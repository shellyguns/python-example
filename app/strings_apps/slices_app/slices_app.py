from app.strings.slices.slices import slices


def main():
    try:
        string = input("Enter a string: ")
        print(slices(string))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
