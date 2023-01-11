# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 01:32:42 2023

@author: KiranR2
"""
from edi_835_parser import parse

path = "C:/Users/KiranR2/Desktop/DataScience/Kiran File/united_healthcare_legacy_sample.txt"

transaction_sets = parse(path)

data = transaction_sets.to_dataframe()

data.to_csv("C:/Users/KiranR2/Desktop/DataScience/Kiran File/my_edi_file.csv",index=False)