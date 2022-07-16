def dividers_quantity(num: int):
    if not isinstance(num, int):
        raise TypeError(f'Argument "num" must be integer, not {type(num)}')
    nums = []
    if num == 0:
        return 1
    if num < 0:
        for i in range(num, - num + 1):
            if i == 0:
                continue
            if num % i == 0:
                nums.append(i)
        return len(nums)
    else:
        for i in range(1, num + 1):
            if num % i == 0:
                nums.append(i)
        return len(nums)
