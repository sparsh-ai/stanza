import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import sys
sys.path.append('../')
from deem import datasets
from datetime import datetime
from deem.utils import load_config, set_logger, print_to_json, print_to_list
from deem.features import FeatureMap
import gc
import argparse
import logging
import os
from pathlib import Path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', type=str, default='pytorch', help='The model version.')
    parser.add_argument('--config', type=str, default='../config/', help='The config directory.')
    parser.add_argument('--expid', type=str, help='The experiment id to run.')
    parser.add_argument('--gpu', type=int, default=-1, help='The gpu index, -1 for cpu')
    
    args = vars(parser.parse_args())
    experiment_id = args['expid']
    params = load_config(args['config'], experiment_id)
    if params.get('version'):
        if params.get('version') != args['version']:
            raise RuntimeError('The config experiment_id={} does not support {}!'\
                               .format(experiment_id, args['version']))
    else:
        params['version'] = args['version']
    if args['version'] == 'tensorflow':
        os.environ["CUDA_VISIBLE_DEVICES"] = str(args['gpu'])
        import tensorflow as tf
        from tensorflow.python.keras import backend as K
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        K.set_session(tf.Session(config=config))
        from deem.tensorflow import models
        from deem.tensorflow.tf_utils import seed_everything
    elif args['version'] == 'pytorch':
        from deem.pytorch import models
        from deem.pytorch.torch_utils import seed_everything
        params['gpu'] = args['gpu']

    set_logger(params)
    logging.info(print_to_json(params))
    seed_everything(seed=params['seed'])

    dataset = params['dataset_id'].split('_')[0].lower()
    data_dir = os.path.join(params['data_root'], params['dataset_id'])
    if params.get("data_format") == 'h5':
        feature_map = FeatureMap(params['dataset_id'], data_dir, params['version'])
        json_file = os.path.join(os.path.join(params['data_root'], params['dataset_id']), "feature_map.json")
        if os.path.exists(json_file):
            feature_map.load(json_file)
        else:
            raise RuntimeError('feature_map not exist!')
    else: 
        try:
            ds = getattr(datasets, dataset)
        except:
            raise RuntimeError('Dataset={} not exist!'.format(dataset))
        feature_encoder = ds.FeatureEncoder(**params)
        if os.path.exists(feature_encoder.json_file):
            feature_encoder.feature_map.load(feature_encoder.json_file)
        else: # Build feature_map and transform h5 data
            datasets.build_dataset(feature_encoder, **params)
        feature_map = feature_encoder.feature_map
        params["train_data"] = os.path.join(data_dir, 'train*.h5')
        params["valid_data"] = os.path.join(data_dir, 'valid*.h5')
        if "test_data" in params:
            params["test_data"] = os.path.join(data_dir, 'test*.h5')
        params["item_corpus"] = os.path.join(data_dir, 'item_corpus.h5')

    model_class = getattr(models, params['model'])
    model = model_class(feature_map, **params)
    model.count_parameters() # print number of parameters used in model
    train_gen, valid_gen = datasets.h5_generator(feature_map, stage='train', **params)
    model.fit(train_gen, valid_generator=valid_gen, **params)
    model.load_weights(model.checkpoint)

    logging.info('****** Train/validation evaluation ******')
    valid_result = model.evaluate(train_gen, valid_gen)
    del valid_gen
    gc.collect()
    
    test_result = dict()
    if "test_data" in params:
        logging.info('******** Test evaluation ********')
        test_gen = datasets.h5_generator(feature_map, stage='test', **params)
        test_result = model.evaluate(train_gen, test_gen)
    
    with open(Path(args['config']).stem + '.csv', 'a+') as fw:
        fw.write(' {},[command] python {},[exp_id] {},[dataset_id] {},[train] {},[val] {},[test] {}\n' \
            .format(datetime.now().strftime('%Y%m%d-%H%M%S'), 
                    ' '.join(sys.argv), experiment_id, params['dataset_id'],
                    "N.A.", print_to_list(valid_result), print_to_list(test_result)))

