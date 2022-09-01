# bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return sorted(arr, reverse=True)

list_to_sort = [1, 5, 6, 3, 4, 8, 2]

print(bubble_sort(list_to_sort))
