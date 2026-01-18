import matplotlib.pyplot as plt

x = [10,1,4,77,12]
y = [2,4,6,8,10]
z = [0,1,2,3,4,5]
plt.plot(y, color = "Cyan", label = "Small line")
plt.plot(x, color="lime", label = "Big line")
plt.title("X vs Y", fontsize = 15)
plt.xlabel("X axis")
plt.ylabel("Y-axis")
plt.legend()
plt.xticks()
plt.show()


#notes
# in plt.plot(x,y) - x is the horizontal line and y is the vertical line 
# quite simple, x = x-axis and y = y axis. EZ right? NO

# Let's say you just enter plt.plot(x,y)
# Now,is it the x-axis or the y-axis?
# It'll be the y axis 
# Then what will be the x axis? It'll be in a default order of 0, 0.5, 1, 1.5, 2 ....

#No how can we remove the increment of 0.5 in the x axis
#Either providing lot of data or, using 
#plt.xticks(variable) and variable = [1,2,3,4,5] or anything you want
