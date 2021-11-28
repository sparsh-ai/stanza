
### Tree
```
.
├── [ 17M]  gnn
│   ├── [ 81K]  Deepwalk
│   │   ├── [1.6K]  dataset.py
│   │   ├── [2.0K]  deepwalk_main.py
│   │   ├── [1.2K]  deepwalk.py
│   │   ├── [ 61K]  ind.citeseer.graph
│   │   ├── [9.8K]  __pycache__
│   │   │   ├── [2.0K]  dataset.cpython-37.pyc
│   │   │   ├── [1.6K]  deepwalk.cpython-37.pyc
│   │   │   └── [2.3K]  utils.cpython-37.pyc
│   │   └── [2.0K]  utils.py
│   ├── [3.8M]  DGI
│   │   ├── [1.8K]  main.py
│   │   ├── [2.0K]  model.py
│   │   ├── [ 16K]  __pycache__
│   │   │   ├── [3.2K]  model.cpython-37.pyc
│   │   │   ├── [6.2K]  process.cpython-37.pyc
│   │   │   └── [2.2K]  utils.cpython-37.pyc
│   │   ├── [3.8M]  self_sup_weight.pth
│   │   └── [1.6K]  utils.py
│   ├── [ 13K]  GAT
│   │   ├── [3.2K]  main.py
│   │   ├── [4.4K]  model.py
│   │   └── [ 893]  utils.py
│   ├── [ 19K]  GCN
│   │   ├── [1.4K]  dataset.py
│   │   ├── [3.0K]  main.py
│   │   ├── [2.3K]  model.py
│   │   ├── [8.0K]  __pycache__
│   │   │   ├── [1.9K]  dataset.cpython-37.pyc
│   │   │   ├── [1.6K]  model.cpython-37.pyc
│   │   │   └── [ 513]  utils.cpython-37.pyc
│   │   └── [ 281]  utils.py
│   ├── [ 18K]  GRACE
│   │   ├── [1.6K]  main.py
│   │   ├── [2.3K]  model.py
│   │   ├── [9.2K]  __pycache__
│   │   │   ├── [3.1K]  model.cpython-37.pyc
│   │   │   └── [2.1K]  utils.cpython-37.pyc
│   │   └── [1.3K]  utils.py
│   ├── [ 72K]  LINE
│   │   ├── [ 65K]  LINE_run.ipynb
│   │   └── [2.3K]  utils.py
│   ├── [ 52K]  metapath2vec
│   │   ├── [ 23K]  metapath2vec.ipynb
│   │   ├── [ 23K]  metapath2vecpp.ipynb
│   │   └── [2.3K]  utils.py
│   └── [ 12M]  TransE
│       ├── [ 12M]  data
│       │   ├── [4.2M]  KG_head.pt
│       │   ├── [4.2M]  KG_label.pt
│       │   └── [4.2M]  KG_tail.pt
│       ├── [1.6K]  dataset.py
│       ├── [2.0K]  main.py
│       ├── [2.0K]  model.py
│       └── [8.2K]  __pycache__
│           ├── [2.3K]  dataset.cpython-37.pyc
│           └── [1.8K]  model.cpython-37.pyc
├── [ 61K]  ind.citeseer.graph
├── [  59]  README.md
└── [ 75M]  rec
    ├── [ 24M]  AutoRec
    │   ├── [ 24M]  data
    │   │   ├── [ 12M]  ml_100k_test.npy
    │   │   └── [ 12M]  ml_100k_train.npy
    │   ├── [ 665]  dataset.py
    │   ├── [2.1K]  main.py
    │   ├── [ 428]  model.py
    │   └── [5.9K]  __pycache__
    │       ├── [1.0K]  dataset.cpython-37.pyc
    │       └── [ 847]  model.cpython-37.pyc
    ├── [ 68K]  BPR
    │   ├── [ 33K]  BPR_kNN.ipynb
    │   └── [ 31K]  BPR_MF.ipynb
    ├── [ 24M]  CDL
    │   ├── [ 24M]  data
    │   │   ├── [ 12M]  ml_100k_test.npy
    │   │   ├── [ 12M]  ml_100k_train.npy
    │   │   └── [232K]  movies.csv
    │   ├── [2.0K]  dataset.py
    │   ├── [1.8K]  main.py
    │   ├── [6.1K]  model.py
    │   └── [ 11K]  __pycache__
    │       ├── [1.2K]  dataset.cpython-37.pyc
    │       └── [5.5K]  model.cpython-37.pyc
    ├── [ 24M]  CML
    │   ├── [ 24M]  data
    │   │   ├── [ 12M]  ml_100k_test.npy
    │   │   ├── [ 12M]  ml_100k_train.npy
    │   │   └── [232K]  movies.csv
    │   └── [7.7K]  main.py
    ├── [ 18K]  FM
    │   ├── [ 10K]  Factorization Machines.ipynb
    │   └── [3.4K]  Untitled0.ipynb
    ├── [ 18K]  intergratedSVD
    │   └── [ 14K]  Intergrated_SVD.ipynb
    ├── [2.1M]  NeuMF
    │   ├── [ 11K]  GMF.ipynb
    │   ├── [ 12K]  MLP.ipynb
    │   ├── [ 14K]  NeuMF.ipynb
    │   └── [2.1M]  pretrained
    │       ├── [515K]  gmf_pretrained.pth
    │       ├── [551K]  mlp_pretrained.pth
    │       └── [1.0M]  NeuMF.pth
    ├── [ 27K]  OCCF
    │   └── [ 23K]  OCCF.ipynb
    ├── [ 11K]  PMF
    │   └── [7.4K]  PMF.ipynb
    ├── [8.7K]  SoRec
    │   └── [4.7K]  main.py
    ├── [ 11K]  SVD++
    │   └── [7.1K]  SVD++.ipynb
    └── [ 18K]  wide _ deep
        └── [ 14K]  wide and deep.ipynb

  92M used in 34 directories, 80 files
```

### Links
- https://github.com/yeonjun-in/GNN_Recsys_paper