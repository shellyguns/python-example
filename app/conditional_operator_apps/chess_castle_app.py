from app.conditional_operator.chess_castle.chess_castle import chess_castle


def main():
    try:
        castle_coordinate1 = input("Enter alphabetical coordinate of castle figure: ")
        castle_coordinate2 = int(input("Enter numerical coordinate of castle figure: "))
        target_coordinate1 = input("Enter alphabetical coordinate of target figure: ")
        target_coordinate2 = int(input("Enter alphabetical coordinate of target figure: "))

        print(chess_castle(castle_coordinate1, castle_coordinate2, target_coordinate1, target_coordinate2))
    except Exception as err:
        print(f"Unexpected error : {err}", err)

