def num_sort(nums: list):
    for num in nums:
        if not isinstance(num, int):
            raise TypeError(f'Argument "num" must be string, not {type(num)}')
    return sorted(nums)
