def chess_castle(castle_coordinate1: str, castle_coordinate2: int, target_coordinate1: str, target_coordinate2: int):
    if not isinstance(castle_coordinate1, str):
        raise TypeError(f'Argument "castle_coordinate1" must be string, not {type(castle_coordinate1)}')
    if not isinstance(castle_coordinate2, int):
        raise TypeError(f'Argument "castle_coordinate2" must be integer, not {type(castle_coordinate2)}')
    if not isinstance(target_coordinate1, str):
        raise TypeError(f'Argument "target_coordinate1" must be string, not {type(target_coordinate1)}')
    if not isinstance(target_coordinate2, int):
        raise TypeError(f'Argument "target_coordinate2" must be integer, not {type(target_coordinate2)}')
    if len(castle_coordinate1) > 1 or len(target_coordinate1) > 1:
        raise ValueError(f'Coordinates should consist of 1 character')
    if castle_coordinate1 == target_coordinate1 and castle_coordinate2 == target_coordinate2:
        raise ValueError(f'Figures can`t be at the same position')
    if castle_coordinate1 < "a" or castle_coordinate1 > "h":
        raise ValueError(f'{castle_coordinate1} should be in range (a, h)')
    if castle_coordinate2 < 1 or castle_coordinate2 > 8:
        raise ValueError(f'{castle_coordinate2} should be in range (1, 8)')
    if target_coordinate1 < "a" or target_coordinate1 > "h":
        raise ValueError(f'{target_coordinate1} should be in range (a, h)')
    if target_coordinate2 < 1 or target_coordinate2 > 8:
        raise ValueError(f'{target_coordinate2} should be in range (1, 8)')
    if castle_coordinate1 == target_coordinate1 or castle_coordinate2 == target_coordinate2:
        return "Yes"
    else:
        return "No"
