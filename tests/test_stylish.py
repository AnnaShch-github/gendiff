from gendiff import generate_diff
from tests import flat_json, flat_yaml, recursion_json, recursion_yaml


def test_flat_json():
    verifiable = generate_diff('tests/fixtures/file1.json',
                               'tests/fixtures/file2.json')
    assert verifiable == flat_json


def test_flat_yaml():
    verifiable = generate_diff('tests/fixtures/file1.yaml',
                               'tests/fixtures/file2.yaml')
    assert verifiable == flat_yaml


def test_flat_yml():
    verifiable = generate_diff('tests/fixtures/file1.yml',
                               'tests/fixtures/file2.yml')
    assert verifiable == flat_yaml


def test_recursion_json():
    verifiable = generate_diff('tests/fixtures/file1_recursion.json',
                               'tests/fixtures/file2_recursion.json')
    assert verifiable == recursion_json


def test_recursion_yaml():
    verifiable = generate_diff('tests/fixtures/file1_recursion.yaml',
                               'tests/fixtures/file2_recursion.yaml')
    assert verifiable == recursion_yaml

def test_recursion_yml():
    verifiable = generate_diff('tests/fixtures/file1_recursion.yml',
                               'tests/fixtures/file2_recursion.yml')
    assert verifiable == recursion_yaml


