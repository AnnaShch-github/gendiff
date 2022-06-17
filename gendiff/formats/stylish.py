EXTENDED_SPACE = ' '
COUNT_INDENT = 4


def stylish(tree, depth):
    result = ['{']
    open_indent = EXTENDED_SPACE * (COUNT_INDENT * depth - 2)
    close_indent = EXTENDED_SPACE * (COUNT_INDENT * (depth - 1))
    for node in tree:
        key = node.get('key')
        value = get_nested_value(node.get('value'), depth + 1)
        if node.get('status') == 'ADDED':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='+', key=key,
                value=value
            ))
        elif node.get('status') == 'DELETED':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='-', key=key,
                value=value
            ))
        elif node.get('status') == 'UNCHANGED':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol=' ', key=key,
                value=value
            ))
        elif node.get('status') == 'NESTED':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol=' ', key=key,
                value=stylish(node.get('value'), depth + 1)
            ))
        else:
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='-', key=key,
                value=value
            ))
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='+', key=key,
                value=get_nested_value(node.get('value2'), depth + 1)
            ))
    result.append('{current_indent}{symbol}'.format(
        current_indent=close_indent, symbol='}'
    ))
    return '\n'.join(result)


def get_nested_value(smth, depth):
    open_indent = EXTENDED_SPACE * (COUNT_INDENT * depth - 2)
    close_indent = EXTENDED_SPACE * (COUNT_INDENT * (depth - 1))
    if isinstance(smth, dict):
        result = ["{"]
        for key, value in smth.items():
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=open_indent, symbol=' ', key=key,
                value=get_nested_value(value, depth + 1)
            ))
        result.append('{EXTENDED_SPACE}{symbol}'.format(
            EXTENDED_SPACE=close_indent, symbol='}'
        ))
        return '\n'.join(result)
    else:
        return smth


def stylish_wrapper(tree):
    return stylish(tree, 1)
