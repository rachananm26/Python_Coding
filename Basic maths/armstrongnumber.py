# number that is equal to the sum of its digits, where each digit is raised to the power of the total number of digits.
num=int(input("Enter a number"))
dup=num
temp= num
count=0
total=0

while temp>0:
    temp=temp//10
    count+=1

while num>0:
    last_digit=num%10
    total=total+(last_digit**count)
    num=num//10
if dup == total:
    print(dup,"is a armstrong number")

else:
    print(dup,"is not a armstrong number")
