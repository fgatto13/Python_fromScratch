# default argument is a default value for certain parameters
# usually it is used when that argument is omitted, therefore making the function more flexible.
# reduces the number of arguments
#
# There are 4 types of parameters:
#
# 1. positional
# 2. default
# 3. keyword
# 4. arbitrary

# to set a default value, we can do that as such:
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 1))