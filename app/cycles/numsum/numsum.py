def numsum(nums: list):
    nsum = 0
    for num in nums:
        if not isinstance(num, int):
            raise TypeError(f'Arguments "num" must be integer, not {type(num)}')
        nsum += num
    return nsum
