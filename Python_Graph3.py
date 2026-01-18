#Barchat and A PROJECT using the barchat function:

import matplotlib.pyplot as plt

plt.title("Strength Of Countries")
Country_name = []
Powerindex = []

for i in range(1,5):
    country = input(f"Enter the name of country {i}: ")
    power = float(input("Enter the power index: "))
    Country_name.append(country)
    Powerindex.append(power)

plt.bar(Country_name, Powerindex)
plt.xlabel("Countries")
plt.ylabel("FirePowerIndex")
plt.show()