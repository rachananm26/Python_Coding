def count(n):
 cnt=0
 while n>0:
    last_digit=n%10
    n=n//10 #anything divisible is log10 big o(n)
    cnt += 1
 print(cnt)

count(int(input("Enter a number")))

"""n % 10 → get last digit
n // 10 → remove last digit
cnt += 1 → count how many times you remove a digit"""