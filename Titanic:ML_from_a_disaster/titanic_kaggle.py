#!/usr/bin/python2.7
from __future__ import print_function
import csv 

def parse_xls(input_file):
    file_handle = open(input_file,'r')
    file_data = file_handle.read()
    file_data = file_data.split("\r\n")
    
    parsed_data = []
    for item in csv.reader(file_data, delimiter=","):
    #    print item 
    #for item in file_data:
    #    item = item.split(",")
        parsed_data.append(item)
    return parsed_data        

def list_to_feature(input_list):
    feature_list = {}
    header = input_list[0]

    for index,feature in enumerate(header):
        feature_list[feature] = [] 

    input_list = input_list[1:len(input_list)-1]
    for item in input_list:
        for index,feature in enumerate(header):
            feature_list[feature].append(item[index])
    return feature_list       

def empty_elements(input_list):
    count = 0
    for item in input_list:
        if (not item):
            count += 1
    return count



file_name = 'train.csv'
input_lst_as_items = parse_xls(file_name)
input_lst_as_features = list_to_feature(input_lst_as_items)
for key in input_lst_as_features:
    print (key, end='')
    print (':', end='')
    print(empty_elements(input_lst_as_features[key]))
