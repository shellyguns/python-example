from app.lists.num_sort.num_sort import num_sort


def main():
    nums = []
    try:
        str_nums = input("Enter numbers: ")
        list_nums = str_nums.split(", ")
        for each_num in list_nums:
            num = int(each_num)
            nums.append(num)

        print(num_sort(nums))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
