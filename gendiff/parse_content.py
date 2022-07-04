import json

import yaml
from yaml.loader import SafeLoader


def parse_content(content):
    if content.startswith('{') or content.startswith('['):
        result = json.loads(content)
    else:
        result = yaml.load(content, Loader=SafeLoader)
    return result
