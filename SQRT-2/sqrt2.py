# G00348436
# Python function called sqrt2 that calculates and
# prints to the screen the square root of 2 to 100 decimal places
def sqrt(x):

    y = 1.0
    # while to estimate the square root
    # method returns the absolute value of number
    while abs(y*y - x) >= 0.0000001:
        # get better approximation for square root
        y -= (y*y - x) / (2*y)
    return y

# calculate the sqrt
y = sqrt(100)

# print result
print(y)
# print result
print(y*y)