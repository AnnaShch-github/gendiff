def plain(tree, path):
    # Function displays the difference describing changes in the text.
    phrase = []
    for i in tree:
        value = i.get('value')
        value2 = i.get('value2')
        status = i.get('status')
        name = i.get('key')
        path.append(name)
        if status == 'ADDED':
            phrase.append(
                "Property '{0}' was added with value: {1}".format(
                    '.'.join(path), get_nested_value(value)))
        if status == 'DELETED':
            phrase.append("Property '{0}' was removed".format('.'.join(path)))
        if status == 'CHANGED':
            phrase.append("Property '{0}' was updated. From {1} to {2}".format(
                '.'.join(path), get_nested_value(value),
                get_nested_value(value2)
            ))
        if status == 'NESTED':
            phrase.append(plain(value, path))
        path.pop()
    return '\n'.join(phrase)


def get_nested_value(value):
    # Function converts values.
    if isinstance(value, dict):
        return '[complex value]'
    elif value == 'false':
        return value
    elif value == 'true':
        return value
    elif value == 'null':
        return value
    elif isinstance(value, int):
        return value
    else:
        return "'{0}'".format(value)


def get_plain_format(tree):
    # The main function of the modul
    return plain(tree, [])
