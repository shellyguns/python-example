from app.strings.h_delete.h_delete import h_delete


def main():
    try:
        h_string = input("Enter a phrase: ")
        print(h_delete(h_string))
    except Exception as err:
        print(f"Unexpected error : {err}", err)

