import json
import yaml
from yaml.loader import FullLoader

from gendiff.formats import wrapper


def generate_diff(first_file, second_file):
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
    return wrapper(result)


def create_tree(file1, file2):
    keys = sorted(list(file1.keys() | file2.keys()))
    result = []
    for key in keys:
        if key not in file1:
            children = {
                'status': 'ADDED', 'key': key,
                'value': file2[key]
            }
        elif key not in file2:
            children = {
                'status': 'DELETED', 'key': key,
                'value': file1[key]
            }
        elif file1[key] == file2[key]:
            children = {
                'status': 'UNCHANGED', 'key': key,
                'value': file2[key]
            }
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            children = {
                'status': 'NESTED', 'key': key,
                'value': create_tree(file1[key], file2[key])
            }
        else:
            children = {
                'status': 'CHANGED', 'key': key,
                'value': file1[key], 'value2': file2[key],
            }
        result.append(children)
    return result
