from gendiff import generate_diff
from tests import json_rec_json, json_flat_json


def test_json_recursive_json():
    verifiable = generate_diff('tests/fixtures/file1_recursion.json',
                               'tests/fixtures/file2_recursion.json',
                               'json')
    assert verifiable == json_rec_json


def test_json_plain_json():
    verifiable = generate_diff('tests/fixtures/file1.json',
                               'tests/fixtures/file2.json',
                               'json')
    assert verifiable == json_flat_json
