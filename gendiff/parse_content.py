import json

import yaml


def parse_content(content):
    if content.startswith('{') or content.startswith('['):
        result = json.loads(content)
    else:
        result = yaml.safe_load(content)
    return result
