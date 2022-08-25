# Write a program that takes as input an array of digits encoding a nonnegative decimal
# integer D and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def increment_one(arr):
    s=""
    for i in arr:
        s += str(i)
    num = int(s)
    newnum = num+1
    result = []
    for i in str(newnum):
        result.append(int(i))
    return result


arr1_list = [1, 2, 9]
print(increment_one(arr1_list))