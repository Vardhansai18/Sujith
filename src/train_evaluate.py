# load train and test data
# train the algorithm
# save the metrics, params

import os
import pandas as pd
import warnings
import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
from get_data import read_params
import argparse
import joblib
import json


def train_eval(config_path):
    config = read_params(config_path)
    test_data_path    = config['split_data']['test_path']
    train_data_path   = config['split_data']['train_path']
    random_state      = config["base"]["random_state"]
    model_dirs        = config['model_dir']

    alpha             = config['estimators']['ElasticNet']['params']['alpha']
    l1_ratio          = config['estimators']['ElasticNet']['params']['l1_ratio']

    target            = [config['base']['target_col']]

    train             = pd.read_csv(train_data_path,sep = ',')
    test              = pd.read_csv(test_data_path,sep = ',')

    train_x           = train_x.drop(target,axis =1)
    train_y           = train[target]

    test_x            = test_x.drop(target,axis=1)
    test_y            = test[target]

if __name__=='__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    split_and_save_data(config_path=parsed_args.config)

