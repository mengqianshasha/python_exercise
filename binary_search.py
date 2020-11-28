def binary_search(sorted_list, num):
    low = 0
    high = len(sorted_list) - 1
    while low < high:
        mid = int((low + high) / 2)
        if num < sorted_list[mid]:
            high = mid - 1
        elif num > sorted_list[mid]:
            low = mid + 1
        else:
            return mid

    if num == sorted_list[low]:
        return low
    else:
        return -1


def binary_search_v2(sorted_list, num):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if num < sorted_list[mid]:
            high = mid - 1
        elif num > sorted_list[mid]:
            low = mid + 1
        else:
            return mid

    return -1
