# Your input is an array of integers,
# and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]


def even_first(input):
    current_first_odd = 0
    for num in input:
        if num%2==0:
            temp = num
            switch_index = input.index(num)-1
            while switch_index >= current_first_odd:
                input[switch_index+1] = input[switch_index]
                switch_index-=1
            input[current_first_odd]=temp
            current_first_odd+=1
    return input

list1 =[7,3,5,6,4,10,3,2]
print(even_first(list1))
