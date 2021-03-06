# Results of weighting experiments (multiclassification)

| Dataset | Source                                          | Size  | NumFeatures | ClassesCount | ClassSizes | AUC-mu | AUC-mu-sqrt-weights | AUC-mu-linear-weights |
|---------|-------------------------------------------------|-------|-------------|--------------|-------|--------------|-----|--------------------|
| Abalone | https://archive.ics.uci.edu/ml/datasets/Abalone | 4177  |  8 | 28   | ** | 0.5238 ± 0.1483      |    0.5249 ± 0.1440    | 0.5215 ± 0.1465 |
| BNG_bridges1000000 | - | 800199 | 12 | 6 | 0: 15.03%; 1: 10.49%; 2: 42.26%; 3: 12.23%; 4: 10.47%; 5: 9.53%; | 0.9700 ± 0.0002 | 0.9700 ± 0.0002 | 0.9689 ± 0.0002 |
| BNG_cmc | - | 44277 | 8 | 3 | 0: 42.95%; 1: 22.70%; 2: 34.35%; | 0.7467 ± 0.0068 | 0.7467 ± 0.0069 | 0.7468 ± 0.0067 |
| BNG_glass | - | 110326 | 8 | 7 | 0: 32.55%; 1: 35.05%; 2: 8.11%; 3: 0.24%; 4: 6.23%; 5: 4.34%; 6: 13.48%; | 0.9559 ± 0.0017 | 0.9552 ± 0.0020 | 0.9539 ± 0.0023 |
| cmc | - | 1183 | 8 | 3 | 0: 42.43%; 1: 22.74%; 2: 34.83%; | 0.7566 ± 0.0304 | 0.7562 ± 0.0308 | 0.7557 ± 0.0326 |
| Covertype10000* | https://archive.ics.uci.edu/ml/datasets/Covertype   | 10000 | 54  | 7 | 1: 37.23%; 2: 48.35%; 3: 5.85%; 4: 0.47%; 5: 1.70%; 6: 2.97%; 7: 3.43%; |   0.9839  ± 0.0029  |   0.9850 ± 0.0027  | 0.9855 ± 0.0021 |
| Wine    | https://archive.ics.uci.edu/ml/datasets/Wine   | 4898 | 11   | 7 | 3: 0.41%; 4: 3.33%; 5: 29.75%; 6: 44.88%; 7: 17.97%; 8: 3.57%; 9: 0.10%;  |  0.8739  ± 0.0321  |      0.8740  ± 0.0308     | 0.8768 ± 0.0257 |

\* real size of covertype dataset is over 500000, 10000 instances were random choosed for the experiment

** 1: 0.02%; 2: 0.02%; 3: 0.36%; 4: 1.36%; 5: 2.75%; 6: 6.20%; 7: 9.36%; 8: 13.60%; 9: 16.50%; 10: 15.18%; 11: 11.66%; 12: 6.39%; 13: 4.86%; 14: 3.02%; 15: 2.47%; 16: 1.60%; 17: 1.39%; 18: 1.01%; 19: 0.77%; 20: 0.62%; 21: 0.34%; 22: 0.14%; 23: 0.22%; 24: 0.05%; 25: 0.02%; 26: 0.02%; 27: 0.05%; 29: 0.02%;