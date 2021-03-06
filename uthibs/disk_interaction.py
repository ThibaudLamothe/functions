import os
import json
import pickle
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def parse_json(path):
    """Given a json_file =path loading it and sending a dictionary back"""
    with open(path) as f:
        data = json.load(f)
    return data


def url_to_json(url):
    """ Given a web url with a json file, returns a dictionary"""
    r = requests.get(url)
    json_file = r.json()
    return json_file


def write_to_json_file(path, file_name, data):
    """Saving as a json file in one line"""
    filePathNameWExt = path + file_name + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


def read_file(file_name='data.txt'):
    """ Example of file name 'data.txt' """
    with open(file_name, "r") as fichier:
        file = fichier.read()
    return file


def get_token(path):
    with open(path, 'r') as file:
        api_key = file.read()
    return api_key


def load_pickle(file_name):
    PICKLE_PATH = parse_json('../src/params.json')['PICKLE_PATH']
    file_path = PICKLE_PATH + file_name
    with open(file_path, 'rb') as pfile:
        my_pickle = pickle.load(pfile)
    return my_pickle


def save_pickle(object_, file_name):
    PICKLE_PATH = parse_json('../src/params.json')['PICKLE_PATH']
    file_path = PICKLE_PATH + file_name
    with open(file_path, 'wb') as pfile:
        pickle.dump(object_, pfile, protocol=pickle.HIGHEST_PROTOCOL)


def list_pickle():
    PICKLE_PATH = parse_json('../src/params.json')['PICKLE_PATH']
    file_list = os.listdir(PICKLE_PATH)
    pickle_list = [i for i in file_list if '.p' in i]
    print(pickle_list)
