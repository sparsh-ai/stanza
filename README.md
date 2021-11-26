# OpenMatch
OpenMatch provides an open source library for candidate item matching with stunning features in configurability, tunability, and reproducibility. 

## Model List

| Publication |    Model   |  Paper                                                                                       |
| :----:|:----------:|:--------------------------------------------------------------------------------------------|
| UAI'09 |   MF-BPR   |      [BPR: Bayesian Personalized Ranking from Implicit Feedback](https://arxiv.org/ftp/arxiv/papers/1205/1205.2618.pdf)                         |
| RecSys'16 | YoutubeDNN |    [Deep Neural Networks for YouTube Recommendations](https://dl.acm.org/doi/10.1145/2959100.2959190)                               |
| CIKM'21 |    MF-CCL / SimpleX    |    SimpleX: A Simple and Strong Baseline for Collaborative Filtering  |


## Get Started

#### Run the demo

The code workflow is structured as follows:

```python
# Set the data config and model config
feature_cols = [{...}] # define feature columns
label_col = {...} # define label column
params = {...} # set data params and model params

# Set the feature encoding specs
feature_encoder = FeatureEncoder(feature_cols, label_col, ...) # define the feature encoder
datasets.build_dataset(feature_encoder, ...) # fit feature_encoder and build dataset 

# Load data generators
train_gen, valid_gen, test_gen = h5_generator(feature_encoder, ...)

# Define a model
model = SimpleX(...)

# Train the model
model.fit(train_gen, valid_gen, ...)

# Evaluation
model.evaluate(test_gen)

```

#### Run the benchmark

For reproducing the experiment result, you can run the benchmarking script with the corresponding config file as follows.

+ --config: The config file that defines the hyper-parameter space.
+ --gpu: The gpu index used for experiment, and -1 for CPU.

```bash
cd benchmarks
python run_param_tuner.py --config Yelp18/SimpleX_yelp18_x0/SimpleX_yelp18_x0_tuner_config.yaml --gpu 0

```

### File Tree
```
.
├── [ 75K]  benchmarks
│   ├── [4.3K]  benchmark.py
│   ├── [ 981]  enumerate_expid_list.py
│   ├── [ 769]  run_expid_list.py
│   ├── [ 789]  run_param_tuner.py
│   └── [ 64K]  Yelp18
│       ├── [5.2K]  MF_BPR_yelp18_x0
│       │   └── [1.2K]  MF_yelp18_x0_tuner_config.yaml
│       ├── [5.2K]  MF_CCL_yelp18_x0
│       │   └── [1.2K]  MF_CCL_yelp18_x0_tuner_config.yaml
│       ├── [ 44K]  SimpleX_yelp18_x0
│       │   ├── [ 38K]  SimpleX_yelp18_x0_001_297a4b82.log
│       │   └── [1.7K]  SimpleX_yelp18_x0_tuner_config.yaml
│       └── [5.5K]  YoutubeDNN_yelp18_x0
│           └── [1.5K]  YoutubeDNN_yelp18_x0_tuner_config.yaml
├── [ 15K]  config
│   ├── [4.9K]  dataset_config
│   │   └── [ 887]  AmazonBooks.yaml
│   └── [6.3K]  model_config
│       ├── [ 164]  common.yaml
│       ├── [ 583]  MF.yaml
│       ├── [ 795]  SimpleX.yaml
│       └── [ 767]  YoutubeDNN.yaml
├── [8.5M]  data
│   ├── [9.7K]  AmazonBooks
│   │   └── [5.7K]  amazonbooks_x0
│   │       └── [1.7K]  DEEM_data_process.py
│   ├── [9.7K]  Gowalla
│   │   └── [5.7K]  gowalla_x0
│   │       └── [1.7K]  DEEM_data_process.py
│   └── [8.5M]  Yelp18
│       └── [8.5M]  yelp18_x0
│           ├── [1.7K]  DEEM_data_process.py
│           ├── [1.9M]  test.txt
│           └── [6.6M]  train.txt
├── [205K]  deem
│   ├── [7.6K]  autotuner.py
│   ├── [ 27K]  datasets
│   │   ├── [ 111]  amazonbeauty.py
│   │   ├── [ 111]  amazonbooks.py
│   │   ├── [ 111]  amazoncds.py
│   │   ├── [ 111]  amazonelectronics.py
│   │   ├── [ 111]  amazonmovies.py
│   │   ├── [ 111]  citeulikea.py
│   │   ├── [7.0K]  data_utils.py
│   │   ├── [ 111]  gowalla.py
│   │   ├── [  94]  __init__.py
│   │   ├── [ 111]  movielens1m.py
│   │   ├── [ 15K]  __pycache__
│   │   │   ├── [ 324]  amazonbooks.cpython-36.pyc
│   │   │   ├── [4.5K]  data_utils.cpython-36.pyc
│   │   │   ├── [4.5K]  data_utils.cpython-37.pyc
│   │   │   ├── [ 320]  gowalla.cpython-36.pyc
│   │   │   ├── [ 233]  __init__.cpython-36.pyc
│   │   │   ├── [ 237]  __init__.cpython-37.pyc
│   │   │   ├── [ 319]  yelp18.cpython-36.pyc
│   │   │   └── [ 323]  yelp18.cpython-37.pyc
│   │   └── [ 111]  yelp18.py
│   ├── [ 17K]  features.py
│   ├── [   0]  __init__.py
│   ├── [6.2K]  metrics.py
│   ├── [5.2K]  preprocess.py
│   ├── [134K]  pytorch
│   │   ├── [ 10K]  data_generator.py
│   │   ├── [   0]  __init__.py
│   │   ├── [ 25K]  layers
│   │   │   ├── [7.4K]  embedding.py
│   │   │   ├── [  67]  __init__.py
│   │   │   ├── [1.7K]  mlp.py
│   │   │   ├── [ 11K]  __pycache__
│   │   │   │   ├── [4.0K]  embedding.cpython-36.pyc
│   │   │   │   ├── [ 178]  __init__.cpython-36.pyc
│   │   │   │   ├── [1.4K]  mlp.cpython-36.pyc
│   │   │   │   └── [1.3K]  sequence.cpython-36.pyc
│   │   │   └── [ 660]  sequence.py
│   │   ├── [ 19K]  losses
│   │   │   ├── [1.1K]  cosine_contrastive_loss.py
│   │   │   ├── [ 324]  __init__.py
│   │   │   ├── [ 580]  mse_loss.py
│   │   │   ├── [ 548]  pairwise_logistic_loss.py
│   │   │   ├── [ 611]  pairwise_margin_loss.py
│   │   │   ├── [ 11K]  __pycache__
│   │   │   │   ├── [1.4K]  cosine_contrastive_loss.cpython-36.pyc
│   │   │   │   ├── [ 502]  __init__.cpython-36.pyc
│   │   │   │   ├── [ 978]  mse_loss.cpython-36.pyc
│   │   │   │   ├── [1000]  pairwise_logistic_loss.cpython-36.pyc
│   │   │   │   ├── [1.0K]  pairwise_margin_loss.cpython-36.pyc
│   │   │   │   ├── [1.0K]  sigmoid_crossentropy_loss.cpython-36.pyc
│   │   │   │   └── [1.0K]  softmax_crossentropy_loss.cpython-36.pyc
│   │   │   ├── [ 605]  sigmoid_crossentropy_loss.py
│   │   │   └── [ 572]  softmax_crossentropy_loss.py
│   │   ├── [ 54K]  models
│   │   │   ├── [ 11K]  base_model.py
│   │   │   ├── [3.6K]  biasMF.py
│   │   │   ├── [  82]  __init__.py
│   │   │   ├── [2.5K]  MF.py
│   │   │   ├── [ 22K]  __pycache__
│   │   │   │   ├── [8.0K]  base_model.cpython-36.pyc
│   │   │   │   ├── [ 205]  __init__.cpython-36.pyc
│   │   │   │   ├── [2.2K]  MF.cpython-36.pyc
│   │   │   │   ├── [5.2K]  SimpleX.cpython-36.pyc
│   │   │   │   └── [2.6K]  YoutubeDNN.cpython-36.pyc
│   │   │   ├── [7.0K]  SimpleX.py
│   │   │   └── [3.7K]  YoutubeDNN.py
│   │   ├── [ 18K]  __pycache__
│   │   │   ├── [7.9K]  data_generator.cpython-36.pyc
│   │   │   ├── [ 110]  __init__.cpython-36.pyc
│   │   │   ├── [ 114]  __init__.cpython-37.pyc
│   │   │   ├── [3.0K]  torch_utils.cpython-36.pyc
│   │   │   └── [3.0K]  torch_utils.cpython-37.pyc
│   │   └── [3.9K]  torch_utils.py
│   └── [3.7K]  utils.py
├── [ 11K]  LICENSE
└── [1.9K]  README.md

 8.8M used in 27 directories, 87 files
```



