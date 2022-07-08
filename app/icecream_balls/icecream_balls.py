def icecream_balls(quantity: int):
    if not isinstance(quantity, int):
        raise TypeError(f'Argument "quantity" must be integer, not {type(quantity)}')
    if quantity < 0:
        raise ValueError(f'Argument "quantity":{type(quantity)} must be bigger than 0')
    if quantity == 3 or quantity == 5:
        return "Yes"
    else:
        return "No"
