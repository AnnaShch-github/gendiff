#!/usr/bin/python3
import json


def generate_diff(first_file, second_file, format=None):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    keys = sorted(list(file1.keys() | file2.keys()))
    #result = {key: compare(key, file1, file2) for key in sorted(keys)}
    result = '{' + '\n'
    for key in keys:
        file1_value = file1.get(key)
        file2_value = file2.get(key)
        if key in file1 and key in file2 and file1_value == file2_value:
            result = result + '     ' + str(key) + ':' + str(file1.get(key)) + '\n'
        if key in file1 and key not in file2:
            result = result + '    ' + '-' + str(key) + ':' + str(file1.get(key)) + '\n'
        if key in file2 and key not in file1:
            result = result + '    ' + '+' + str(key) + ':' + str(file2.get(key)) + '\n'
        if key in file1 and key in file2 and file1_value != file2_value:
            result = result + '    ' + '-' + str(key) + ':' + str(file1.get(key)) + '\n'
            result = result + '    ' + '+' + str(key) + ':' + str(file2.get(key)) + '\n'
    result = result + '}'
    return result


#def compare(key, file1, file2):
    #file1_value = file1.get(key)
    #file2_value = file2.get(key)
    #if key in file1 and key in file2 and file1_value == file2_value:
    #    dict = file1.get(key)
    #if key in file1 and key not in file2:
    #    dict = file1.get(key)
    #if key in file2 and key not in file1:
    #    dict = file2.get(key)
    #if key in file1 and key in file2 and file1_value != file2_value:
    #    dict = file2.get(key)
    #return dict

