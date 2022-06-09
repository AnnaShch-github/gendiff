import json
import yaml
from yaml.loader import FullLoader


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
    keys = sorted(list(file1.keys() | file2.keys()))
    res = ['{']
    for key in keys:
        unify1 = unify_values(file1.get(key))
        unify2 = unify_values(file2.get(key))
        if key not in file1:
            res.append('{indent}{symbol} {key}: {value}'.format(
                indent='  ', symbol='+', key=key, value=unify2
            ))
        elif key not in file2:
            res.append('{indent}{symbol} {key}: {value}'.format(
                indent='  ', symbol='-', key=key, value=unify1
            ))
        elif file1[key] == file2[key]:
            res.append('{indent}{symbol} {key}: {value}'.format(
                indent='  ', symbol=' ', key=key, value=unify1
            ))
        elif isinstance(key, dict):
            generate_diff(file1[key], file2[key])
        else:
            res.append('{indent}{symbol} {key}: {value}'.format(
                indent='  ', symbol='-', key=key, value=unify1
            ))
            res.append('{indent}{symbol} {key}: {value}'.format(
                indent='  ', symbol='+', key=key, value=unify2
            ))
    res.append('}')
    return '\n'.join(res)


def unify_values(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    else:
        return value
