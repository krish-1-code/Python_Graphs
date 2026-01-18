#In this graph we will be making a scatter plot of IQ vs Testostrone
# Data aren't accurate 

import matplotlib.pyplot as plt

IQ = [80,90,100,110,120,130,140,150,160,170,180]
Testo = [950,900,880,830,790,740,700,640,590,990,1100]

plt.scatter(IQ,Testo, color = "red", s = 150)
plt.show()
