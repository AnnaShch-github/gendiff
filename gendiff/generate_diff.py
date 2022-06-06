import json


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    keys = sorted(list(file1.keys() | file2.keys()))
    res = '{' + '\n'
    for key in keys:
        file1_value = file1.get(key)
        file2_value = file2.get(key)
        unify1 = unify_values(file1_value)
        unify2 = unify_values(file2.get(key))
        if key in file1 and key in file2 and file1_value == file2_value:
            res = res + '    ' + str(key) + ':' + ' ' + str(unify1) + '\n'
        if key in file1 and key not in file2:
            res = res + '  ' + '- ' + str(key) + ':' + ' ' + str(unify1) + '\n'
        if key in file2 and key not in file1:
            res = res + '  ' + '+ ' + str(key) + ':' + ' ' + str(unify2) + '\n'
        if key in file1 and key in file2 and file1_value != file2_value:
            res = res + '  ' + '- ' + str(key) + ':' + ' ' + str(unify1) + '\n'
            res = res + '  ' + '+ ' + str(key) + ':' + ' ' + str(unify2) + '\n'
    res = res + '}'
    return res


def unify_values(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    else:
        return value
