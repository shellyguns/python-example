def bigger_of_two(num1: int, num2: int):
    if not isinstance(num1, int):
        raise TypeError(f'Argument "num1" must be integer, not {type(num1)}')
    if not isinstance(num2, int):
        raise TypeError(f'Argument "num2" must be integer, not {type(num2)}')
    if num1 > num2:
        return num1
    else:
        return num2
