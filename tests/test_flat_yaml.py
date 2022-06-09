from gendiff import generate_diff
from tests import flat_yaml


def test_flat_yaml():
    verifiable = generate_diff('file1.yaml',
                               'file2.yaml')
    assert verifiable == flat_yaml


def test_flat_yml():
    verifiable = generate_diff('file1.yml',
                               'file2.yml')
    assert verifiable == flat_yaml
