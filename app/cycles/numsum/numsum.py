def numsum(nums: list):
    if not isinstance(nums, list):
        raise TypeError(f'Arguments "nums" must be list, not {type(nums)}')
    nsum = 0
    for num in nums:
        if not isinstance(num, int):
            raise TypeError(f'Arguments "num" must be integer, not {type(num)}')
        nsum += num
    return nsum
