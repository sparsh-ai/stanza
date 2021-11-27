## Sign-Aware Recommendation Systems with Graph Neural Networks (SiReN)

### This is PyTorch implementation code for our paper:

> C. Seo et al., SiReN: Sign-Aware Recommendation Using Graph Neural Networks, 
>
> [Paper in arXiv](https://arxiv.org/abs/2108.08735)

Note. In this implementation, we use LightGCN (X. He et al., SIGIR'20) as the GNN model for the graph with positive edges in SiReN.


### Example : ML-1M dataset

```python
python main.py --dataset ML-1M --version 1 --reg 0.1
```

### Example : Amazon-Book dataset

```python
python main.py --dataset amazon --version 1 --reg 0.05
```

### Example : Yelp dataset

```python
python main.py --dataset yelp --version 1 --reg 0.05
```

### Tree
```
.
├── [1.2K]  convols.py
├── [2.4K]  data_loader.py
├── [5.5K]  evaluator.py
├── [5.7K]  main.py
├── [ 766]  README.md
├── [3.4K]  siren.py
└── [3.4K]  util.py

  26K used in 0 directories, 7 files
```

### Links
- https://github.com/woni-seo/siren-reco