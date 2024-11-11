def find_maximum_difference(a, b):
    #code implementation here...
    max_a = max(a)
    max_b = max(b)

    if max_a > max_b:
        min_value = min(b)
        max_value = max_a
    else:
        min_value = min(a)
        max_value = max_b

    maximum = max_value - min_value

    return maximum

result = find_maximum_difference([1, 5, 600], [100, 7, 3, 29, 39]) #600 - 3 = 597
print(result)

result = find_maximum_difference([1, 5 ,600], [100 ,7, 3 , 602, 39]) #602 - 1 = 601
print(result)



