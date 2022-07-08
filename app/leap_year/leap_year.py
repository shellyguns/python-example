def leap_year(year: int):
    if not isinstance(year, int):
        raise TypeError(f'Argument "year" must be integer, not {type(year)}')
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return "Yes"
    else:
        return "No"
