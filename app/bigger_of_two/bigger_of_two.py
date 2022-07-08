def bigger_of_two(num1: int, num2: int):
    if not isinstance(num1, int):
        raise TypeError(f'Argument "a" must be integer, not {type(num1)}')
    if not isinstance(num2, int):
        raise TypeError(f'Argument "b" must be integer, not {type(num2)}')
    return max(num1, num2)