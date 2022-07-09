def dividers(num: int):
    if not isinstance(num, int):
        raise TypeError(f'Argument "num" must be integer, not {type(num)}')
    nums = []
    for i in range(1, num+1):
        if num % i == 0:
            nums.append(i)
    return nums
