from gendiff import generate_diff
from tests import flat_yaml


def test_flat_yaml():
    verifiable = generate_diff('tests/fixtures/file1.yaml',
                               'tests/fixtures/file2.yaml')
    assert verifiable == flat_yaml


def test_flat_yml():
    verifiable = generate_diff('tests/fixtures/file1.yml',
                               'tests/fixtures/file2.yml')
    assert verifiable == flat_yaml
