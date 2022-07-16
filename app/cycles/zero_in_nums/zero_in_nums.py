def zero_in_nums(nums: list):
    for num in nums:
        if not isinstance(num, int):
            raise TypeError(f'Arguments "num" must be integer, not {type(num)}')
    if 0 in nums:
        return "Yes"
    else:
        return "No"
