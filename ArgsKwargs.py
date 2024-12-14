def changer(*args, **kwargs):
    result = {}
    for i, arg in enumerate(args, 1):
        result[f'positional_{i}'] = arg

    for key, value in kwargs.items():
        result[key] = value

    return result
