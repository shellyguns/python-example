from app.lists.greatest_num.greatest_nums import greatest_nums


def main():
    nums = []
    try:
        str_nums = input("Enter numbers: ")
        list_nums = str_nums.split(", ")
        for each_num in list_nums:
            num = int(each_num)
            nums.append(num)

        print(greatest_nums(nums))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
