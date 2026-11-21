# num=89800
# while num>0:
#     reverse=num%10
#     num=num//10
#     print(reverse,end="")

num=998000
rev=0
while num>0:
    lastdigit=num%10
    num=num//10
    rev=rev*10+lastdigit
print(rev)