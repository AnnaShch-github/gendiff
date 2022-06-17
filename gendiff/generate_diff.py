import json
import yaml
from yaml.loader import FullLoader

from gendiff.formats.plain import plain_wrapper
from gendiff.formats.stylish import stylish_wrapper


def generate_diff(first_file, second_file, format='stylish'):
    if first_file[-5] == '.json':
        with open(first_file) as fh:
            file1 = json.load(open(fh))
        with open(second_file) as fh:
            file2 = json.load(open(fh))
    else:
        with open(first_file) as fh:
            file1 = yaml.load(fh, Loader=FullLoader)
        with open(second_file) as fh:
            file2 = yaml.load(fh, Loader=FullLoader)
    result = create_tree(file1, file2)
    if format == 'stylish':
        return stylish_wrapper(result)
    if format == 'plain':
        return plain_wrapper(result)
    raise TypeError("bad format")


def create_tree(file1, file2):
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
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value
