def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """



    # Function implementation here ...

    total = 0   
    for num in range(min, max + 1):  #For loop that gets everynumber in between the given min and max         
        if num % 2 == 0:  #If statement that adds together the even numbers 
            total += num
    
    return total

min = 10
max = 13
result = sum_of_evens(min, max)  #Call the function
print(f"{result} is your sum!")  #Print the sum

# # # Run code example
# min_value = 10
# max_value = 13
# result = sum_of_evens(min_value, max_value) # returns 22
