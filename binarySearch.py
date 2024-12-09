def LinearSearch(number_list,number_to_find):
    for index,element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1


def BinarySearch(number_list,number_to_find):
    left = 0
    right = len(number_list) - 1
    mid_index = 0 

    while left <= right:
        mid_index = (left + right) // 2
        mid = number_list[mid_index] 

        if mid == number_to_find:
            return mid_index
        
        if mid < number_to_find:
            left = mid_index + 1

        else:
            right = mid_index - 1
        return  BinarySearch(number_list,number_to_find)

    return -1




        









if __name__ == '__main__':
    number_list = [2,4,5,6,6,6,7,8,9]
    number_to_find = 6
    index = BinarySearch(number_list,number_to_find)
    print(index)

