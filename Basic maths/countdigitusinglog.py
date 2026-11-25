import math

n = int(input("Enter a number: "))

cnt = int(math.log10(n)) + 1

print("Number of digits:", cnt)