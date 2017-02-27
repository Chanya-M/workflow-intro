def plus_minus(arr):
    greater_than_one = 0
    less_than_one = 0
    zero = 0
    for i in arr:
        if i > 0:
            greater_than_one += 1
        elif i < 0:
            less_than_one += 1
        elif i == 0:
            zero += 1
    positive_values = float(greater_than_one/len(arr))
    negative_values = float(less_than_one/len(arr))
    zeroes = float(zero/len(arr))
    return positive_values, negative_values, zeroes