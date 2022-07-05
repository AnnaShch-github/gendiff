EXTENDED_SPACE = ' '
COUNT_INDENT = 4


def stylish(tree, depth):
    # Function displays the difference describing changes in the string.
    result = ['{']
    open_indent = EXTENDED_SPACE * (COUNT_INDENT * depth - 2)
    close_indent = EXTENDED_SPACE * (COUNT_INDENT * (depth - 1))
    for node in tree:
        key = node.get('key')
        value = format_value(node.get('value'), depth + 1)
        type = node.get('type')
        if type == 'ADDED':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='+', key=key,
                value=value
            ))
        elif type == 'DELETED':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol='-', key=key,
                value=value
            ))
        elif type == 'UNCHANGED':
            result.append('{current_indent}{symbol} {key}: {value}'.format(
                current_indent=open_indent, symbol=' ', key=key,
                value=value
            ))
        elif type == 'NESTED':
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
                value=format_value(node.get('value2'), depth + 1)
            ))
    result.append('{current_indent}{symbol}'.format(
        current_indent=close_indent, symbol='}'
    ))
    return '\n'.join(result)


def format_value(node, depth):
    # Function converts values.
    open_indent = EXTENDED_SPACE * (COUNT_INDENT * depth - 2)
    close_indent = EXTENDED_SPACE * (COUNT_INDENT * (depth - 1))
    if isinstance(node, dict):
        result = ["{"]
        for key, value in node.items():
            result.append('{EXTENDED_SPACE}{symbol} {key}: {value}'.format(
                EXTENDED_SPACE=open_indent, symbol=' ', key=key,
                value=format_value(value, depth + 1)
            ))
        result.append('{EXTENDED_SPACE}{symbol}'.format(
            EXTENDED_SPACE=close_indent, symbol='}'
        ))
        return '\n'.join(result)
    else:
        return node


def get_stylish_format(tree):
    # The main function of the modul
    return stylish(tree, 1)
