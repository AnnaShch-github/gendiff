from gendiff import generate_diff
from tests import recursion_yaml


def test_recursion_yaml():
    verifiable = generate_diff('tests/fixtures/file1_recursion.yaml',
                               'tests/fixtures/file2_recursion.yaml')
    assert verifiable == recursion_yaml

def test_recursion_yml():
    verifiable = generate_diff('tests/fixtures/file1_recursion.yml',
                               'tests/fixtures/file2_recursion.yml')
    assert verifiable == recursion_yaml
