from app.bigger_of_two.bigger_of_two import bigger_of_two


def main():
    try:
        num1 = int(input("Enter number num1: "))
        num2 = int(input("Enter number num2: "))

        print("Bigger number is " + str(bigger_of_two(num1, num2)))
    except Exception as err:
        print(f"Unexpected error : {err}")
