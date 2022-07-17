def print_even_nums(num1: int, num2: int):
    if not isinstance(num1, int):
        raise TypeError(f'Argument "num1" must be integer, not {type(num1)}')
    if not isinstance(num2, int):
        raise TypeError(f'Argument "num2" must be integer, not {type(num2)}')
    if num1 > num2:
        raise ValueError(f'Argument "num1"{num1} must be less than "num2"{num2}')

    nums = []
    for i in range(num1+1, num2):

        if i % 2 == 0:
            nums.append(i)
    if 0 in nums:
        nums.remove(0)
    return nums


# alternative
'''
nums = []
num1 = -5
num2 = 12
i = num1 + 1

while num1 < i < num2:
    if i % 2 == 0:
        nums.append(i)
    i += 1
if 0 in nums:
    nums.remove(0)
    
print(nums)
'''
