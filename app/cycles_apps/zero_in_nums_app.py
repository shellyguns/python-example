from app.cycles.zero_in_nums.zero_in_nums import zero_in_nums


def main():
    nums = []
    try:
        str_nums = input("Enter numbers: ")
        list_nums = str_nums.split(", ")
        for each_num in list_nums:
            num = int(each_num)
            nums.append(num)

        print(zero_in_nums(nums))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
