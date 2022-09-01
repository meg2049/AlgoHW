# selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return sorted(arr, reverse=True)

list_to_sort = [1, 6, 4, 8, 9, 2, 3]
print(selection_sort(list_to_sort))
