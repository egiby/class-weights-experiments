import yaml
import os

import pandas as pd
import numpy as np

from catboost import cv, Pool


class DatasetSettings:
    def __init__(self):
        self.target_column = None
        self.positive_class_range = None
        self.id_column = None
        self.has_header = False
        self.sep = ','
        self.cat_features = []
    
    def is_valid(self):
        return self.target_column is not None and self.positive_class_range is not None
    
    def __str__(self):
        return str(self.__dict__)


def parse_positive_class(value):
    classes = list(map(int, value.split('-')))
    assert len(classes) == 2 or len(classes) == 1, 'bad PositiveClass value'
    if len(classes) == 1:
        classes.append(classes[0] + 1)
    
    return tuple(classes)


def create_dataset_settings(config):
    raw_settings = config['DatasetSettings']
    settings = DatasetSettings()
    
    assert 'Target' in raw_settings
    assert 'PositiveClass' in raw_settings
    settings.target_column = raw_settings['Target']
    settings.positive_class_range = parse_positive_class(str(raw_settings['PositiveClass']))

    if 'ID' in raw_settings:
        settings.id_column = raw_settings['ID']
    
    if 'HasHeader' in raw_settings:
        settings.has_header = raw_settings['HasHeader']
    
    if 'Separator' in raw_settings:
        settings.sep = raw_settings['Separator']
    
    if 'CatFeatures' in raw_settings:
        settings.cat_features = raw_settings['CatFeatures']
    
    assert settings.is_valid()
    return settings


def load_dataset(path, dataset_params=None, multiclass=False):
    if dataset_params is None:
        dataset_root, _ = os.path.split(path)
        with open(os.path.join(dataset_root, 'config.yaml')) as config_file:
            config = yaml.safe_load(config_file)
        
        dataset_params = create_dataset_settings(config)
    
    data = pd.read_csv(path, 
        sep=dataset_params.sep, 
        index_col=dataset_params.id_column,
        header='infer' if dataset_params.has_header else None,
    ).dropna()

    assert dataset_params.target_column is not None, 'target column should be specified'
    y = data[dataset_params.target_column]

    if dataset_params.positive_class_range is not None and not multiclass:
        left, right = dataset_params.positive_class_range
        y = np.logical_and(y >= left, y < right)
    
    x_columns = list(data.columns)
    x_columns.remove(dataset_params.target_column)

    return data[x_columns], y, dataset_params.cat_features


def train_test_dataset(X, y, cat_features=None, auto_class_weights=None, 
                       loss_function='Logloss', iterations=2000, metrics=['AUC']):
    pool = Pool(data=X,
                label=y,
                cat_features=cat_features)
    params = {
        'task_type': 'CPU',
        'auto_class_weights': auto_class_weights,
        'custom_metric': metrics,
        'verbose': False,
        'loss_function': loss_function,
        'iterations': iterations
    }
    
    return cv(
        pool,
        params,
        fold_count=5,
        plot=True,
        logging_level='Info'
    )