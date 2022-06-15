EXTENDED_SPACE = '  '


def stylish(tree, depth):
    result = ['{']
    current_indent = EXTENDED_SPACE * depth
    for node in tree:
        value = get_nested_value(node.get('value'), depth)
        if node.get('status') == 'ADDED':
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=current_indent, symbol='+', key=node.get('key'),
                value=value
            ))
        elif node.get('status') == 'DELETED':
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=current_indent, symbol='-', key=node.get('key'),
                value=value
            ))
        elif node.get('status') == 'UNCHANGED':
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=current_indent, symbol=' ', key=node.get('key'),
                value=value
            ))
        elif node.get('status') == 'NESTED':
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=current_indent, symbol=' ', key=node.get('key'),
                value=stylish(node.get('value'), depth + 1)
            ))
        else:
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=current_indent, symbol='-', key=node.get('key'),
                value=value
            ))
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=current_indent, symbol='+', key=node.get('key'),
                value=get_nested_value(node.get('value2'), depth + 1)
            ))
    result.append('{EXTENDED_SPACE}{symbol}'.format(
        EXTENDED_SPACE=EXTENDED_SPACE * (depth - 1), symbol='}'
    ))
    return '\n'.join(result)


def unify_values(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def get_nested_value(smth, depth):
    if isinstance(smth, dict):
        result = ["{"]
        for key, value in smth.items():
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=EXTENDED_SPACE * depth, symbol=' ', key=key,
                value=get_nested_value(value, depth + 1)
            ))
        result.append('{EXTENDED_SPACE}{symbol}'.format(
            EXTENDED_SPACE=EXTENDED_SPACE * depth, symbol='}'
        ))
        return '\n'.join(result)
    else:
        return unify_values(smth)


def wrapper(list):
    return stylish(list, 1)


