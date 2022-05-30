#!/usr/bin/python3
import json


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    print(open(first_file))
    file2 = json.load(open(second_file))
    keys = list(file1.keys() | file2.keys())
    result = [compare(key, file1, file2) for key in sorted(keys)]
    return result


def compare(key, file1, file2):
    file1_value = file1.get(key)
    file2_value = file2.get(key)
    str_key = str(key)
    str_file2_value = str(file2_value)
    str_file1_value = str(file1_value)
    if key in file1 and key in file2 and file1_value == file2_value:
        string = str_key + ':' + str_file1_value
        string1 = string + '\n'
    if key in file1 and key not in file2:
        string = '+' + str_key + ':' + str_file1_value
        string1 = string + '\n'
    if key in file2 and key not in file1:
        string = '-' + str_key + ':' + str_file2_value
        string1 = string + '\n'
    if key in file1 and key in file2 and file1_value != file2_value:
        string = '+' + str_key + ':' + str_file1_value + '\n' + '-' + str_key + ':' + str_file2_value
        string1 = string + '\n'
    return string1

