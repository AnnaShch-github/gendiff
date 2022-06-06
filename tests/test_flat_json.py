from gendiff import generate_diff
import expected


def test_flat_json():
    verifiable = generate_diff('/home/anna/python-project-lvl2/file1.json',
                               '/home/anna/python-project-lvl2/file2.json')
    assert verifiable == expected.flat_json