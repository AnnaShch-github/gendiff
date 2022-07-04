import pytest
from gendiff import generate_diff


@pytest.mark.parametrize('file1, file2, format, expected', [
    ('tests/fixtures/file1_recursion.json',
     'tests/fixtures/file2_recursion.json',
     'json',
     'tests/fixtures/expected_json_rec_json.txt'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'json',
     'tests/fixtures/expected_json_flat_json.txt'),
    ('tests/fixtures/file1_recursion.json',
     'tests/fixtures/file2_recursion.json',
     'plain',
     'tests/fixtures/expected_plain_rec_json.txt'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'plain',
     'tests/fixtures/expected_plain_flat_json.txt'),
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.json',
     'stylish',
     'tests/fixtures/expected_flat_json.txt'),
    ('tests/fixtures/file1.yaml',
     'tests/fixtures/file2.yaml',
     'stylish',
     'tests/fixtures/expected_flat_yaml.txt'),
    ('tests/fixtures/file1_recursion.json',
     'tests/fixtures/file2_recursion.json',
     'stylish',
     'tests/fixtures/expected_rec_json.txt'),
    ('tests/fixtures/file1_recursion.yaml',
     'tests/fixtures/file2_recursion.yaml',
     'stylish',
     'tests/fixtures/expected_rec_yaml.txt'),
    ('tests/fixtures/file1_recursion.yml',
     'tests/fixtures/file2_recursion.yml',
     'stylish',
     'tests/fixtures/expected_rec_yaml.txt')
])
def test_gendiff(file1, file2, format, expected):
    with open(expected, 'r') as f1:
        result = f1.read()
    assert generate_diff(file1, file2, format) == result
