import yaml
import json


def _read_config(path='./confing/configuration.yaml'):
    with open(path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def read_config(path='./config/configuration.yaml'):
    api_key =  _read_config(path)['API_KEY']
    api_secret = _read_config(path)['API_SECRET']
    return api_key, api_secret


def save_json(dic, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(dic, file, ensure_ascii=False, indent=4)


def load_json(file_name):
    with open(file_name, 'r') as file:
        dic = json.load(file)
        return dic
