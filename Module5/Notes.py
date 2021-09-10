import numpy as np
import numpy.random
import pandas as pd
import matplotlib.pyplot as plt

#implicit X-axis values from 0 to (N-1) where N is length of the list


'''
y = [1, 2, 3, 4, 5, 6]
print([i**3 for i in y])
plt.plot([i**3 for i in y],y)
plt.show()
'''

'''
x = np.arange(0,3,0.1)
print(x)
plt.plot(x,[i**2 for i in x])
plt.show()
'''


#Multiple Line Plot
'''
x = range(5)
plt.plot(x,[i**3 for i in x])
plt.plot(x,[j**2 for j in x])
plt.plot(x,[k*5 for k in x])
plt.show()
plt.show()
plt.show()
'''


#To Show the Grid in the background
'''
x = np.arange(0,3,0.1)
print(x)
plt.plot(x,[i**2 for i in x])
plt.grid(True)
plt.show()
'''

#Limiting the AXes - to see the limited Coordinates in the Graph
'''
x = range(5)
plt.plot(x,[i**3 for i in x])
plt.plot(x,[j**2 for j in x])
plt.plot(x,[k*5 for k in x])
#plt.axis([0, 0.5, 0, 0.5])
plt.xlim(0, 3)
plt.ylim(0, 3)
plt.show()
plt.show()
plt.show()
'''
#Note: The Scale of the plot can be set using xlim() and ylim()


#Adding Labels to Plot and Title to the plot
'''
x = np.arange(0,3,0.1)
print(x)
plt.plot(x,[i**2 for i in x])
plt.grid(True)
plt.xlabel('DevOps')
plt.ylabel('Python')
plt.title('Learning python')
plt.show()
'''

#Adding Legends to the plt - Legend : explains the meaning of each Line in the graph
'''
x = range(5)
plt.plot(x,[i**3 for i in x],label='CUBE')
plt.plot(x,[j**2 for j in x],label='Square')
plt.plot(x,[k*5 for k in x],label='Multiple')
plt.legend()
plt.xlabel('DevOps')
plt.ylabel('Python')
plt.title('Learning python')
plt.show()
plt.show()
plt.show()
#NOTE : to Save the plot : Syntax : plt.savefig('Plot.png')
#plt.savefig('Plot.png')
'''

#Types of Plots
#Matplotlib provides many types of plot formats for visualising Information
"""
1:Scatter Plot 2: Histogram 3:Bar Graph 4:Pie Chart
"""

#Histogram - Distribution of Variable over a range of frequencies or values
#numpy.random.randn
"""
y = numpy.random.randn(10, 10)  #10x10 array of a Gaussian Distribution
plt.hist(y, 100)  #Function to plot the histogram takes the dataset as the parameter
plt.show()
"""

#BAR CHART
#Should provide Two array, First array is midpoint of the bar Graph
'''

plt.bar([1,2,5],[10,20,30])
plt.show()
'''


'''
d1 = {'a':2,'b':4,'c':6}
for i,key in enumerate(d1):
    plt.bar(i,d1[key])
plt.xticks([1,2,3],d1.keys())  #Used to place the labels on the Bar Graph
plt.show()
'''

#PIE CHART
'''
plt.figure(figsize=(4,4))
plt.pie([25,50,75,100],labels=['Python','Java','C++','ML'])
plt.show()
'''


#SCATTER PLOT --> Scatter plots Display values for two Sets of data, visualised as a collection of points
#VALUES are generated as Gaussian Distribution values
'''
x = numpy.random.rand(20)   #if the values of X and Y doesn't match, it will throw a error, bcoz neither Y or X coordinates will not meet 
y = numpy.random.randn(20)
print(x,y)
plt.scatter(x,y)
plt.show()
'''






