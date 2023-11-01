def remove_duplicates_and_sort(arr):
    unique_arr = list(set(arr))
    unique_arr.sort()
    return unique_arr
array_with_duplicates = [3, 2, 1, 2, 3, 5, 4, 6, 5, 4, 7]
result = remove_duplicates_and_sort(array_with_duplicates)
print("Array with duplicates removed and sorted:", result)




