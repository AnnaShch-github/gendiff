from gendiff import generate_diff
from tests import recursion_json


def test_recursion_json():
    verifiable = generate_diff('tests/fixtures/file1_recursion.json',
                               'tests/fixtures/file2_recursion.json')
    assert verifiable == recursion_json
