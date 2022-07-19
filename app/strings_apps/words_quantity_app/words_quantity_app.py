from app.strings.words_quantity.words_quantity import words_quantity


def main():
    try:
        words = input("Enter words separated with spaces: ")
        print(words_quantity(words))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
