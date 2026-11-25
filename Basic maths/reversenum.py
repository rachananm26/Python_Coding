rev=0
num=int(input("enter a number"))
while num>0:
    lastdigit=num%10
    num=num//10
    rev=rev*10+lastdigit
print(rev)

#
# num % 10 → Extract the last digit.
# num // 10 → Remove the last digit.
# rev * 10 + last_digit → Append the extracted digit to the reversed number.