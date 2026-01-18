#In this graph I'll be making a pie chart which depicts the time spent by a college student


import matplotlib.pyplot as plt

activities = ["Studying","Social Media","Cooking","Socializing","Out-door activities","Other things"]
time = []
x = 24
plt.title("Time Management", fontsize = 30)
for i in range(0,6):
    times = int(input(f"How much time do you spend in {activities[i]} out of {x} hrs: "))
    x -= times
    time.append(times)

plt.pie(time, labels = activities,
              autopct = "%1.1f%%",
              shadow = True)
plt.legend()
plt.show()