def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """


    # Function implementation here ...

    if num <= 1:
        return False
    if num <= 3:
        return True 
    if num % 2 == 0 or num % 3 == 0:
        return  False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return  False
        i += 6

    output = True
    return output
      
#print (is_prime(7))

boolean = is_prime(5) #True
print(boolean)
boolean = is_prime(9) #False
print(boolean)
boolean = is_prime(13) #True
print(boolean)
        
        
# # # Run code example
# boolean = is_prime(5)   # returns True
# print(boolean)
  