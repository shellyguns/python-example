from app.icecream_balls.icecream_balls import icecream_balls


def main():
    try:
        quantity = int(input("Enter a quantity: "))
        print(icecream_balls(quantity))
    except Exception as err:
        print(f"Unexpected error : {err}")