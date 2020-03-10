def get_value(obj, path='', delimiter='.'):
    tokens = path.split(delimiter)
    target_value = obj
    for token in tokens:
        target_value = target_value.get(token)

    return target_value
