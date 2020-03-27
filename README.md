# Results of weighting experiments

[Multiclassification results](multiclass.md)

## Binary classification

| Dataset | Source                                          | Size  | NumFeatures | PositiveClass | PositiveProportion | IsMulticlass | AUC | AUC-linear-weights | AUC-sqrt-weights |
|---------|-------------------------------------------------|-------|----|--------------|--------------------|--------------|-----|--------------------|------------------|
| Abalone | https://archive.ics.uci.edu/ml/datasets/Abalone | 4177  |  8 | merged 16-27 | 6.2%               | true         |    0.8934  ± 0.0110   |    0.8936 ± 0.0124    |   0.8918 ± 0.0128    | 
| Amazon  | catboost.datasets                               | 32771 |  9 |  0           | 5.7%               | false        |   0.8441  ± 0.0062   |        0.8415  ± 0.0085    |   0.8422  ± 0.0089    |
| Adult   | https://archive.ics.uci.edu/ml/datasets/Adult   | 32561 | 14 |  >50K        | 24.1%              | false        |    0.9298  ± 0.0033   |     0.9297  ± 0.0037   |      0.9300  ± 0.0032              |
| Covertype10000* | https://archive.ics.uci.edu/ml/datasets/Covertype   | 10000 | 54 |  merged 4-7        | 8.5%              | true        |   0.9561  ± 0.0095    |          0.9560  ± 0.0098            |        0.9567  ± 0.0095        |
| Wine    | https://archive.ics.uci.edu/ml/datasets/Wine   | 4898 | 11 |  merged 8-10   | 3.6%              | true        |  0.9070  ± 0.0149  |  0.8998  ± 0.0145  |    0.9025  ± 0.0113   |


*real size of covertype dataset is over 500000, 10000 instances were random choosed for the experiment
