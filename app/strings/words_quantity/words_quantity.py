def words_quantity(words: str):
    if not isinstance(words, str):
        raise TypeError(f'Argument "words" must be string, not {type(words)}')
    words_list = words.split()
    return len(words_list)

"""
    spaces = 0
    for space in words:
        if space == " ":
            spaces += 1
    words_q = spaces + 1
    return words_q
"""
