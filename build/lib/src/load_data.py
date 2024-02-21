import os
import argparse
from get_data import read_config,get_config

def load_and_save(config_path):
    config=read_config(config_path)
    df=get_config(config_path)
    new_cols=[cols.replace(' ','_') for cols in df.columns]
    raw_data_path=config['load_data']['raw_dataset_csv']
    df.to_csv(raw_data_path,sep=",",index=False,header=new_cols)
   # print(df.columns)

if __name__=='__main__':
    args=argparse.ArgumentParser()
    args.add_argument('--config_path',default='params.yaml')
    parser=args.parse_args()
    load_and_save(parser.config_path)
