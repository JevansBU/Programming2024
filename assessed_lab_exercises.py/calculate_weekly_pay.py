def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay

    # Function implementation here ...

#If and Elif statements to calculate the pay depending on if its regular or overtime rates V
    if hours_worked <= 35:
        total_pay = hours_worked * 12
        return total_pay
    elif hours_worked > 35:
        total_pay = (hours_worked - 35) * 18 + (35 * 12)
        return total_pay

    return total_pay

regular_pay = calculate_weekly_pay(17)
print(f"£{regular_pay} is how much You've earned this week!")
overtime_pay = calculate_weekly_pay(38)
print(f"£{overtime_pay} is how much You've earned this week!")

# # Code Example
# overtime_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
# print(overtime_pay)
