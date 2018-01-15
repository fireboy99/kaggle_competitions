#!/usr/bin/python2.7
def parse_xls(input_file):
    file_handle = open(input_file,'r')
    file_data = file_handle.read()
    file_data = file_data.split("\r\n")
    
    parsed_data = []
    for item in file_data:
        item = item.split(",")
        parsed_data.append(item)
    return parsed_data        

def list_to_feature(input_list):
    feature_list = {}
    header = input_list[0]

    for index,feature in enumerate(header):
        feature_list[feature] = input_list[1][index]
        print feature, input_list[1][index] 
    print feature_list

    input_list = input_list[2:len(input_list)]
    for item in input_list:
        for index,feature in enumerate(header):
            feature_list[feature].append(item[index])
    return feature_list       

file_name = 'train.csv'
input_lst_as_items = parse_xls(file_name)
input_lst_as_features = list_to_feature(input_lst_as_items)
#print(input_lst_as_items[0][0])
