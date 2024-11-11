def annual_net_income(gross_salary):
    # complete your function implementation here...

    if gross_salary >= 45000:
        net_salary = 0.5 * gross_salary
    elif 30000 <= gross_salary and gross_salary < 45000:
        net_salary = 0.7 * gross_salary
    elif gross_salary < 30000:
        net_salary = 0.85 * gross_salary

    return net_salary
        

print(annual_net_income(60000)) #30000
print(annual_net_income(30000)) #21000
print(annual_net_income(20000)) #17000



