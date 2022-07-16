def even_els(nums: list):
    even_nums = []
    for num in nums:
        if not isinstance(num, int):
            raise TypeError(f'Argument "num" must be string, not {type(num)}')
        if num % 2 == 0:
            even_nums.append(num)
        if 0 in even_nums:
            even_nums.remove(0)
    return even_nums

