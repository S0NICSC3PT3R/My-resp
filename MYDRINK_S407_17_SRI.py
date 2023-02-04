a_list = ["PowerBoost", "EnergyOne", "RedOx", "VitaJuice", "HydroPlus"]
print (a_list)

search = input("Enter a drink: ")
if search in a_list: print("Drink found. Enjoy!")
else:print("Drink not found.")