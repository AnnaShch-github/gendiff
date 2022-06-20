import json
import yaml
from yaml.loader import FullLoader

from gendiff.formats.json import get_json_format
from gendiff.formats.plain import get_plain_format
from gendiff.formats.stylish import get_stylish_format


def generate_diff(first_file, second_file, format='stylish'):
    # Function reads the data and return the difference between them
    if first_file[-5] == '.json':
        with open(first_file) as f1:
            file1 = json.load(open(f1))
        with open(second_file) as f2:
            file2 = json.load(open(f2))
    else:
        with open(first_file) as f1:
            file1 = yaml.load(f1, Loader=FullLoader)
        with open(second_file) as f2:
            file2 = yaml.load(f2, Loader=FullLoader)
    result = create_tree(file1, file2)
    if format == 'stylish':
        return get_stylish_format(result)
    if format == 'plain':
        return get_plain_format(result)
    if format == 'json':
        return get_json_format(result)
    raise TypeError("bad format")


def create_tree(file1, file2):
    # Build the list of the dictionaries containing analysis of the difference
    keys = sorted(list(file1.keys() | file2.keys()))
    result = []
    for key in keys:
        value1 = unify_values(file1.get(key))
        value2 = unify_values(file2.get(key))
        if key not in file1:
            children = {
                'status': 'ADDED', 'key': key,
                'value': value2
            }
        elif key not in file2:
            children = {
                'status': 'DELETED', 'key': key,
                'value': value1
            }
        elif file1[key] == file2[key]:
            children = {
                'status': 'UNCHANGED', 'key': key,
                'value': value2
            }
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            children = {
                'status': 'NESTED', 'key': key,
                'value': create_tree(value1, value2)
            }
        else:
            children = {
                'status': 'CHANGED', 'key': key,
                'value': value1, 'value2': value2,
            }
        result.append(children)
    return result


def unify_values(value):
    # Function unify boolean values from different formats
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value
