def h_delete(h_string: str):
    if not isinstance(h_string, str):
        raise TypeError(f'Argument "h_string" must be string, not {type(h_string)}')
    h = []
    for i in range(len(h_string)):
        if h_string[i] == "h":
            h.append(i)
    return h_string.replace(h_string[h[0]:h[-1]+1], "")
