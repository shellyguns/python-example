def unique(nums: list):
    unique_values = []
    for num in nums:
        if not isinstance(num, int):
            raise TypeError(f'Argument "num" must be string, not {type(num)}')
        if nums.count(num) == 1:
            unique_values.append(num)
    return unique_values
