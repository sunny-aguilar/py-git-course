#!/usr/bin/env python3

# return factorial of n
def bang(n):
    if n is 0:
	    return 1
    return n * bang(n-1)


n = 35          # number of users
result = 0      # probability result

# calculate probability that ten or fewer are active at the same time
for k in range(11):
    # probability that exactly k users are active
    probabilityOfSet = pow(0.1, k) * pow(0.9, n - k)
    numberOfSets = bang(35)/(bang(35 - k) * bang(k)) # n choose k
    result += probabilityOfSet * numberOfSets


# modify so result is the probability that 11 or more people are
# active at the same time00
result = 1 - result

# display result
print(result)

