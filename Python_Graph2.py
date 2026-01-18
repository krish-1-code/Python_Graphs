# We'll be making a grpah showing the spread of covid-19
# We'll take the reproduction number to be 1.6 

import matplotlib.pyplot as plt
import math

Remaining_pop = []
Infected_pop = []

plt.title("Spread of a disease", fontsize = 30, color = "grey")
plt.xlabel("Years")
plt.ylabel("Population")
Initial_pop = int(input("Enter the starting population: "))

R0 = 1.6
Time = int(input("Enter the time in years: "))

for i in range(Time):

    Current_pop = int(Initial_pop * math.exp(-R0*i))
    Remaining_pop.append(Current_pop)
    Infected_pop.append(Initial_pop-Current_pop)

plt.plot(Remaining_pop, color = "blue",
                        linewidth = 5,
                        label = "Non-infected People",
                        marker = ".",
                        ms = 20)
plt.plot(Infected_pop, color = "red",
                        linewidth = 5,
                        label = "Infected People",
                        marker = "*",
                        ms = 20)
plt.legend()
plt.show()