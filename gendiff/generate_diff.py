from gendiff.formats.get_formats import get_format
from gendiff.formats.unify_values import unify_values
from gendiff.parse_content import parse_content


def generate_diff(first_file, second_file, format='stylish'):
    # Function reads the data and return the difference between them
    with open(first_file, 'r') as f1, open(second_file, 'r') as f2:
        file1 = f1.read()
        file2 = f2.read()
    result = create_tree(parse_content(file1), parse_content(file2))
    return get_format(format, result)


def create_tree(content1, content2):
    # Build the list of the dictionaries containing analysis of the difference
    keys = sorted(list(content1.keys() | content2.keys()))
    result = []
    for key in keys:
        value1 = unify_values(content1.get(key))
        value2 = unify_values(content2.get(key))
        if key not in content1:
            children = {
                'type': 'ADDED', 'key': key,
                'value': value2
            }
        elif key not in content2:
            children = {
                'type': 'DELETED', 'key': key,
                'value': value1
            }
        elif content1[key] == content2[key]:
            children = {
                'type': 'UNCHANGED', 'key': key,
                'value': value2
            }
        elif isinstance(content1[key], dict) and isinstance(
                content2[key], dict):
            children = {
                'type': 'NESTED', 'key': key,
                'value': create_tree(value1, value2)
            }
        else:
            children = {
                'type': 'CHANGED', 'key': key,
                'value': value1, 'value2': value2,
            }
        result.append(children)
    return result
