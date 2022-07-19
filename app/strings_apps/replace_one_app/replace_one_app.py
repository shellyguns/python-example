from app.strings.replace_one.replace_one import replace_one


def main():
    try:
        phrase = input("Enter a phrase: ")
        print(replace_one(phrase))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
