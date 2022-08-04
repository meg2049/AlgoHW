# Count odd and even numbers. Count odd and even digits of the whole number.

n=572386

even =[int(x) for x in str(n) if int(x)%2 ==0]
odd = [int(x) for x in str(n) if int(x)%2]
print("Even numbers are",even)
print("Odd numbers are",odd)
