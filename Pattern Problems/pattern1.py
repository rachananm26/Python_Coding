def pattern(n):# n is the size of the pattern
    for i in range(n):          # outer loop → rows ,range() when we want to generate a sequence of number,repeat the line n times
        for j in range(n):      # inner loop → columns
            print("*", end=" ")
        print()                 # move to the next line

pattern(10)                  # for a single n

# for n in [2, 4, 6]:            # multiple n values,[2, 4, 6] is a list, and the for loop goes through each value in that list one by one.
#     pattern(n)                # reusing the same function for different pattern sizes.