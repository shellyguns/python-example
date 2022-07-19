from app.lists.even_index.even_index import even_index


def main():
    nums = []
    try:
        str_nums = input("Enter numbers: ")
        list_nums = str_nums.split(", ")
        for each_num in list_nums:
            num = int(each_num)
            nums.append(num)

        print(even_index(nums))
    except Exception as err:
        print(f"Unexpected error : {err}", err)
