from gendiff import generate_diff
import expected


def test_flat_json():
    verifiable = generate_diff('file1.json',
                               'file2.json')
    assert verifiable == expected.flat_json