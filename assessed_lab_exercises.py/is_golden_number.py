def is_golden_number(n):

    # function implementation ...

    boolean = False
    for a in range(1, n):
        b = n - a
        if a * b % 1000 == 0:
            boolean = True
            break

    return boolean

result = is_golden_number(65) #True
print(result)
result = is_golden_number(70) #True
print(result)
result = is_golden_number(23) #False
print(result)
