def slices(string: str):
    if not isinstance(string, str):
        raise TypeError(f'Argument "string" must be string, not {type(string)}')
    return string[2], string[-2], string[:4], string[:-2], string[2::2], string[1::2], string[::-1], len(string)
