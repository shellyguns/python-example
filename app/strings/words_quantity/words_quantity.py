def words_quantity(words: str):
    if not isinstance(words, str):
        raise TypeError(f'Argument "words" must be string, not {type(words)}')
    words_list = words.split()
    return len(words_list)
