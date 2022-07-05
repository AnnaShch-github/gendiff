from gendiff.formats.json import get_json_format
from gendiff.formats.plain import get_plain_format
from gendiff.formats.stylish import get_stylish_format


def get_format(format, tree):
    # Choose the format
    if format == 'stylish':
        return get_stylish_format(tree)
    if format == 'plain':
        return get_plain_format(tree)
    if format == 'json':
        return get_json_format(tree)
    raise TypeError("bad format")
