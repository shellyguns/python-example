from app.cycles.dividers_quantity.dividers_quantity import dividers_quantity


def main():
    try:
        num = int(input("Enter a number: "))

        print(dividers_quantity(num))
    except Exception as err:
        print(f"Unexpected error : {err}", err)