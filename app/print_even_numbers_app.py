from app.print_even_nums.print_even_nums import print_even_nums


def main():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(print_even_nums(num1, num2))
    except Exception as err:
        print(f"Unexpected error : {err}")
