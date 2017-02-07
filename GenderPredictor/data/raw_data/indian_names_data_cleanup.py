#!/usr/bin/env python3.5
# encoding: utf-8

from string import punctuation, digits
import pprint
import re
import random

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
        
        
def data_process(file_name='', gender='F', output_file='female_names_parsed.txt'):
    _content = ''
    invalid_chars = set(punctuation + digits)
    _dict = AutoVivification()
    import csv
    with open(file_name, encoding='utf8') as csv_file:
        _content = csv.reader(csv_file, delimiter=',')

        for _value in _content:
            _value = _value[0]
            _value = _value.strip()
            if any(char in invalid_chars for char in _value):
                for invalid_char in invalid_chars:
                    if invalid_char in _value:
                        tmp = _value.replace(invalid_char, ' ')
                        _value = ''.join(tmp).strip()
                # re.sub(r'\s+', '')
                _value = [i for i in _value.split(' ') if len(i) > 1]
                
            names = _value
            for name in names:
                name = name.strip()
                if not len(name) >= 2:
                    continue
                if not all(ord(char) < 128 for char in name):
                    continue
                if name in _dict.keys():
                    _dict[name]['count'] += random.randint(10, 100)
                else:
                    _dict[name]['count'] = random.randint(100, 1000)
                    _dict[name]['gender'] = gender

        # pprint.pprint(_dict)

        output_file = open(output_file, encoding='utf-8', mode='w')
        for _name in _dict.keys():
            output_file.write(_name + ',' + _dict[_name]['gender'] + ',' + str(_dict[_name]['count']) + '\n')
        output_file.close()
        del _dict


female_file = 'Indian-Female-Names.csv'
male_file = 'Indian-Male-Names.csv'
data_process(file_name=male_file, gender='M', output_file='indian_male_names_parsed.txt')
data_process(file_name=female_file, gender='F', output_file='indian_female_names_parsed.txt')
