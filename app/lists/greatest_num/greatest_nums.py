def greatest_nums(nums: list):
    for num in nums:
        if not isinstance(num, int):
            raise TypeError(f'Argument "num" must be string, not {type(num)}')
    return max(nums), nums.index(max(nums))
