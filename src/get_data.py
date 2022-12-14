## read the params
## process
## return the dataframe

import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)
    return config
def get_data(config_path):
    config = read_params(config_path)
    #print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path,sep=',',encoding='utf-8')
    return df

if __name__=='__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--m",default="params.yaml")
    print(args)
    #parsed_args = args.parse_args()
    #get_data(config_path=parsed_args.config)
    