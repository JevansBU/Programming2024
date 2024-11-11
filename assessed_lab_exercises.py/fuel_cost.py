def fuel_cost(distance_miles):
#     # Constants

    MPG = 50  # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  # Price in pounds per liter

#     continue function implementation here...

    total_cost = PRICE_PER_LITER * (distance_miles/MPG) * LITERS_PER_GALLON

    return total_cost

print(f"£{fuel_cost(50)}") #£6.705
print(f"£{fuel_cost(20)}") #£2.682
print(f"£{fuel_cost(120)}") #£16.092








