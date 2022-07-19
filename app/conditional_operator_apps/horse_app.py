from app.conditional_operator.horse.horse import horse


def main():
    try:
        horse_coordinate1 = input("Enter alphabetical coordinate of horse figure: ")
        horse_coordinate2 = int(input("Enter numerical coordinate of horse figure: "))
        target_coordinate1 = input("Enter alphabetical coordinate of target figure: ")
        target_coordinate2 = int(input("Enter alphabetical coordinate of target figure: "))

        print(horse(horse_coordinate1, horse_coordinate2, target_coordinate1, target_coordinate2))
    except Exception as err:
        print(f"Unexpected error : {err}", err)

