import os
import argparse
import yaml
import pandas as pd

def read_config(config_path):
    with open(config_path) as config:
        yaml_config= yaml.safe_load(config)
    return yaml_config

def get_config(config_path):
    config=read_config(config_path)
    data_path=config['data_source']['s3_source']
    df=pd.DataFrame(pd.read_csv(data_path,sep=',',encoding='utf-8'))
    return df
    print(df.head())

if __name__=='__main__':

    args=argparse.ArgumentParser()
    args.add_argument('--data_path',default='params.yaml')
    parser=args.parse_args()

    data=get_config(config_path=parser.data_path)
