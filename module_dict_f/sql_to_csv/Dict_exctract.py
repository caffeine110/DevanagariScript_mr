#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 23:48:07 2018


@author: gaurav gahukar


AIM     : to create DICT.csv file

        : input  : exctracted.csv
        : output : Dict.csv


"""

import pandas as pd

filename = 'exctracted.csv'
data = pd.read_csv(filename, delimiter=",", usecols=['word'])
print(data)

data.columns
data['stemed'] = ''
filepath = 'Dict.csv'
data.to_csv(filepath, index=False)