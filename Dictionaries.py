#Dictionaries
#Worked Example VVV
'''my_dict = {"name": "John",
           "age": 25,
           "is_student": True,
           "sleep_late": False,
           "descriptive_message": "John is a student who likes programming" }
print(my_dict)'''

#Exercise 1 VVV

carDict = {"car_make": "Peugeot",
           "car_model": "108 Active",
           "millage": 42000,
           "colour": "Navy Blue",
           "engine": 1.0}        #Dictionary of my old car
print(carDict)                #Prints the details of carDict
make = carDict["car_make"] #Assign a value from the dictionary to a separate variable
print(carDict)
carDict["millage"] = 43000 #Modify a value in the dictionary
print(carDict)
carDict["Doors"] = 5 #Adds a new value to the dictionary
print(carDict)
del carDict["engine"] #Deletes a value from the dictionary
print(carDict)
