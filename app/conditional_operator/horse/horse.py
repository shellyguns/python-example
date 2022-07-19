def horse(horse_coordinate1: str, horse_coordinate2: int, target_coordinate1: str, target_coordinate2: int):
    if not isinstance(horse_coordinate1, str):
        raise TypeError(f'Argument "horse_coordinate1" must be string, not {type(horse_coordinate1)}')
    if not isinstance(horse_coordinate2, int):
        raise TypeError(f'Argument "horse_coordinate2" must be integer, not {type(horse_coordinate2)}')
    if not isinstance(target_coordinate1, str):
        raise TypeError(f'Argument "target_coordinate1" must be string, not {type(target_coordinate1)}')
    if not isinstance(target_coordinate2, int):
        raise TypeError(f'Argument "target_coordinate2" must be integer, not {type(target_coordinate2)}')
    if len(horse_coordinate1) > 1 or len(target_coordinate1) > 1:
        raise ValueError(f'Coordinates should consist of 1 character')
    if horse_coordinate1 == target_coordinate1 and horse_coordinate2 == target_coordinate2:
        raise ValueError(f'Figures can`t be at the same position')
    if horse_coordinate1 < "a" or horse_coordinate1 > "h":
        raise ValueError(f'{horse_coordinate1} should be in range (a, h)')
    if horse_coordinate2 < 1 or horse_coordinate2 > 8:
        raise ValueError(f'{horse_coordinate2} should be in range (1, 8)')
    if target_coordinate1 < "a" or target_coordinate1 > "h":
        raise ValueError(f'{target_coordinate1} should be in range (a, h)')
    if target_coordinate2 < 1 or target_coordinate2 > 8:
        raise ValueError(f'{target_coordinate2} should be in range (1, 8)')
    distance_a = abs(ord(horse_coordinate1) - ord(target_coordinate1))
    distance_n = abs(horse_coordinate2 - target_coordinate2)
    if (distance_a == 1 and distance_n == 2) or (distance_a == 2 and distance_n == 1):
        return "Yes"
    else:
        return "No"
