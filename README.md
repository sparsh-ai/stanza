# SGL
This is our Tensorflow implementation for our SIGIR 2021 paper:

>Jiancan Wu, Xiang Wang, Fuli Feng, Xiangnan He, Liang Chen, Jianxun Lian,and Xing Xie. 2021. Self-supervised Graph Learning for Recommendation, [Paper in arXiv](https://arxiv.org/abs/2010.10783).

## Environment Requirement

The code runs well under python 3.7.7. The required packages are as follows:

- Tensorflow-gpu == 1.15.0
- numpy == 1.19.1
- scipy == 1.5.2
- pandas == 1.1.1
- cython == 0.29.21

## Quick Start
**Firstly**, compline the evaluator of cpp implementation with the following command line:

```bash
python setup.py build_ext --inplace
```

If the compilation is successful, the evaluator of cpp implementation will be called automatically.
Otherwise, the evaluator of python implementation will be called.

**Note that the cpp implementation is much faster than python.**

Further details, please refer to [NeuRec](https://github.com/wubinzzu/NeuRec/)

**Secondly**, specify dataset and recommender in configuration file *NeuRec.properties*.

Model specific hyperparameters are in configuration file *./conf/SGL.properties*.

Some important hyperparameters (taking a 3-layer SGL-ED as example):

### yelp2018 dataset
```
aug_type=1
reg=1e-4
embed_size=64
n_layers=3
ssl_reg=0.1
ssl_ratio=0.1
ssl_temp=0.2
```

### amazon-book dataset
```
aug_type=1
reg=1e-4
embed_size=64
n_layers=3
ssl_reg=0.5
ssl_ratio=0.1
ssl_temp=0.2
```

### ifashion dataset
```
aug_type=1
reg=1e-3
embed_size=64
n_layers=3
ssl_reg=0.02
ssl_ratio=0.4
ssl_temp=0.5
```


**Finally**, run [main.py](./main.py) in IDE or with command line:

```bash
python main.py --recommender=SGL
```

## Tree
```
.
├── [4.5K]  conf
│   └── [ 468]  SGL.properties
├── [ 46K]  data
│   ├── [ 12K]  dataset.py
│   ├── [ 286]  __init__.py
│   ├── [ 26K]  sampler.py
│   └── [3.2K]  utils.py
├── [ 55K]  evaluator
│   ├── [ 987]  abstract_evaluator.py
│   ├── [ 39K]  backend
│   │   ├── [ 21K]  cpp
│   │   │   ├── [1.4K]  cpp_evaluator.pyx
│   │   │   ├── [8.3K]  include
│   │   │   │   ├── [1.7K]  evaluate.h
│   │   │   │   └── [2.6K]  metric.h
│   │   │   └── [7.4K]  uni_evaluator.py
│   │   ├── [ 223]  __init__.py
│   │   └── [ 14K]  python
│   │       ├── [2.3K]  metric.py
│   │       └── [7.7K]  uni_evaluator.py
│   ├── [5.0K]  grouped_evaluator.py
│   ├── [  44]  __init__.py
│   └── [5.2K]  proxy_evaluator.py
├── [1.8K]  main.py
├── [ 37K]  model
│   ├── [2.8K]  AbstractRecommender.py
│   └── [ 30K]  general_recommender
│       └── [ 26K]  SGL.py
├── [ 977]  NeuRec.properties
├── [1.6K]  README.md
├── [  59]  requirements.txt
├── [ 917]  setup.py
└── [ 50K]  util
    ├── [5.9K]  configurator.py
    ├── [ 16K]  cython
    │   ├── [1.0K]  arg_topk.pyx
    │   ├── [7.7K]  include
    │   │   ├── [1.1K]  arg_topk.h
    │   │   └── [2.7K]  thread_pool.h
    │   ├── [2.5K]  random_choice.pyx
    │   └── [ 882]  tools.pyx
    ├── [4.9K]  data_generator.py
    ├── [6.8K]  data_iterator.py
    ├── [ 517]  __init__.py
    ├── [1.7K]  learner.py
    ├── [2.1K]  logger.py
    └── [8.5K]  tool.py

 202K used in 12 directories, 35 files
```

## Links
- https://github.com/wujcan/SGL