def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    # Function implementation here ...

    total = 0
    sum = 0
    for number in numbers:   #Loops through contents of 'numbers' and adds them all together 
        total += number
        sum = sum + 1
    
    average = total/sum    #Obtains the average of the list and then divides the total of the numbers by the average
    
    return average

sum = 0
print(f"The average is: {calculate_average([10, 20, 30, 40, 50])}") #30.0
print(f"The average is: {calculate_average([1, 3, 7, 5, 0])}") #3.2

# # Example usage
# numbers = [10, 20, 30, 40, 50]
# print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0
