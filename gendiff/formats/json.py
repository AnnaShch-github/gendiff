import json


def get_json_format(tree):
    # This function return the result in json format
    return json.dumps(tree, indent=4)
