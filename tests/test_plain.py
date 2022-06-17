from gendiff import generate_diff
from tests import plain_recursive_json, plain_flat_json


def test_plain_recursive_json():
    verifiable = generate_diff('tests/fixtures/file1_recursion.json',
                               'tests/fixtures/file2_recursion.json',
                               'plain')
    assert verifiable == plain_recursive_json


def test_flat_plain_json():
    verifiable = generate_diff('tests/fixtures/file1.json',
                               'tests/fixtures/file2.json',
                               'plain')
    assert verifiable == plain_flat_json
