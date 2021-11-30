
## Code

This is the source code for SIGIR 2020 Paper: _Global Context Enhanced Graph Neural Networks for Session-based Recommendation_.

## Requirements

- Python 3
- PyTorch >= 1.3.0
- tqdm

## Usage

Data preprocessing:

The code for data preprocessing can refer to [SR-GNN](https://github.com/CRIPAC-DIG/SR-GNN).

Train and evaluate the model:
~~~~
python build_graph.py --dataset diginetica --sample_num 12
python main.py --dataset diginetica
~~~~

## Citation

~~~~
@inproceedings{wang2020global,
    title={Global Context Enhanced Graph Neural Networks for Session-based Recommendation},
    author={Wang, Ziyang and Wei, Wei and Cong, Gao and Li, Xiao-Li and Mao, Xian-Ling and Qiu, Minghui},
    booktitle={Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval},
    pages={169--178},
    year={2020}
}
~~~~

## Tree
```
.
├── [3.6K]  aggregator.py
├── [1.5K]  build_graph.py
├── [4.2K]  main.py
├── [8.3K]  model.py
├── [ 919]  README.md
└── [3.5K]  utils.py

  26K used in 0 directories, 6 files
```

## Links
- https://github.com/CCIIPLab/GCE-GNN