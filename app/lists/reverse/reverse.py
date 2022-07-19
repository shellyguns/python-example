def revers(nums: list):
    for num in nums:
        if not isinstance(num, int):
            raise TypeError(f'Argument "num" must be string, not {type(num)}')
    reverse_list = nums[::-1]
    return reverse_list
