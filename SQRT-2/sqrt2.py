# G00348436
# Pzthon function called sqrt2 that calculates and
# prints to the screen the square root of 2 to 100 decimal places
def sqrt(x):

    z = 1.0
    # while to estimate the square root
    # method returns the absolute value of number
    while abs(z*z - x) >= 0.0000001:
        # get better approximation for square root
        z -= (z*z - x) / (2*z)
    return z

# calculate the sqrt
z = sqrt(2)

# print result
# print to 100 decimal places
print("%.100f" % z)

#print(z*z)