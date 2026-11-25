#any number divisible only 1 and itself

def primenumber(n):
    if n<=1:
        print("Its not a prime number")
        return
    i=2
    while i*i<=n:
        if n%i==0:
         print(n,"is not a prime number")
         return
        i+=1

    print(n,"is a prime number")

primenumber(7)