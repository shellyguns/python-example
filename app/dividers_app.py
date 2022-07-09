from app.dividers.dividers import dividers


def main():
    try:
        num = int(input("Enter a number: "))

        print(dividers(num))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
