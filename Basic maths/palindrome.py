
num=int(input("Enter a number"))
temp=num
rev=0
while num>0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10
if temp==rev:
    print(rev,"is a palindrome")
else:
    print(rev,"is not a palindrome")