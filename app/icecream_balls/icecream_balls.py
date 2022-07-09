def icecream_balls(quantity: int):
    if not isinstance(quantity, int):
        raise TypeError(f'Argument "quantity" must be integer, not {type(quantity)}')
    if quantity < 0:
        raise ValueError(f'Argument "quantity":{quantity} must be bigger than 0')
    if quantity % 3 == 0 or quantity % 5 == 0 or quantity % (3 + 5) == 0:
        return "Yes"
    else:
        return "No"
