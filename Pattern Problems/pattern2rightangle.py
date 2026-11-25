def pattern2(n):
    for i in range(1,n+1): #since n starts from 1 start it should not be n range ,n range starts from 0 to n,n+1 exculdes last value
        for j in range(i): #number of start in row
            print("*",end=" ")
        print()
pattern2(8)
# for n in [3,6,8]:
#     pattern2(n)