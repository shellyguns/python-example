from app.leap_year.leap_year import leap_year


def main():
    try:
        year = int(input("Enter a year: "))
        print(leap_year(year))
    except Exception as err:
        print(f"Unexpected error : {err}")
