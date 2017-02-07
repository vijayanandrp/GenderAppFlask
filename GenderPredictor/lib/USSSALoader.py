#!/usr/bin/env python3.5
# encoding: utf-8

"""
    USSSALoader.py
"""

import os
from zipfile import ZipFile
from urllib import request
from lib.config import zip_file, name_pickle_file as pickle_file
import pickle


def download_names():
    u = request.urlopen('https://github.com/downloads/sholiday/genderPredictor/names.zip')
    with open(zip_file, 'wb') as file:
        file.write(u.read())
    
    
def extract_names_dict():
    zf = ZipFile(zip_file, 'r')
    file_names = zf.namelist()
    names = dict()
    gender_map = {'M': 0, 'F': 1}
    for file_name in file_names:
        file = zf.open(file_name, 'r').read().decode('utf-8')
        infile = file.split('\n')
        rows = [row.strip().split(',') for row in infile if len(row) > 1]
        for row in rows:
            name = row[0].upper()
            gender = gender_map[row[1].upper()]
            count = int(row[2])
            if name not in names:
                names[name] = [0, 0]
            names[name][gender] += count
    return names
            
            
def get_name_list():
    if not os.path.exists(pickle_file):
       
        if not os.path.exists(zip_file):
            download_names()
            
        names_dict = extract_names_dict()
        
        male_names = list()
        female_names = list()
        
        for name in names_dict:
            counts = names_dict[name]
            data = (name, counts[0], counts[1])
            if counts[0] > counts[1]:
                male_names.append(data)
            elif counts[1] > counts[0]:
                female_names.append(data)
        
        names = (male_names, female_names)
        fw = open(pickle_file, 'wb')
        pickle.dump(names, fw, -1)
        fw.close()
    else:
        f = open(pickle_file, 'rb')
        names = pickle.load(f)
            
    return names
    

if __name__ == "__main__":
    get_name_list()
