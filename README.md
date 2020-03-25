# Results of weighting experiments

| Dataset | Source                                          | Size  | NumFeatures | PositiveClass | PositiveProportion | IsMulticlass | AUC | AUC-linear-weights | AUC-sqrt-weights | AUC-mu | AUC-mu-sqrt-weights |
|---------|-------------------------------------------------|-------|----|--------------|--------------------|--------------|-----|--------------------|------------------|--------|---------------------|
| Abalone | https://archive.ics.uci.edu/ml/datasets/Abalone | 4177  |  8 | merged 16-27 | 6.2%               | true         |   $0.8934 \pm 0.0110$  |   $0.8936 \pm 0.0124$   |  $0.8918 \pm 0.0128$   |   $0.5238 \pm 0.1483$     |   $0.5249 \pm 0.1440$   |
| Amazon  | catboost.datasets                               | 32771 |  9 |  0           | 5.7%               | false        |  $0.8441 \pm 0.0062$  |       $0.8415 \pm 0.0085$   |  $0.8422 \pm 0.0089$   |        |                     |
| Adult   | https://archive.ics.uci.edu/ml/datasets/Adult   | 32561 | 14 |  >50K        | 24.1%              | false        |   $0.9298 \pm 0.0033$  |    $0.9297 \pm 0.0037$  |     $0.9300 \pm 0.0032$             |        |                     |
| Covertype10000* | https://archive.ics.uci.edu/ml/datasets/Covertype   | 10000 | 54 |  merged 4-7        | 8.5%              | true        |  $0.9561 \pm 0.0095$   |         $0.9560 \pm 0.0098$           |       $0.9567 \pm 0.0095$       |  $0.9839 \pm 0.0029$ |                     |
| Wine    | https://archive.ics.uci.edu/ml/datasets/Wine   | 4898 | 11 |  merged 8-10   | 3.6%              | true        | $0.9070 \pm 0.0149$ | $0.8998 \pm 0.0145$ |   $0.9025 \pm 0.0113$  |   $0.8739 \pm 0.0321$ |     $0.8740 \pm 0.0308$    |


*real size of covertype dataset is over 500000, 10000 instances were random choosed for the experiment
