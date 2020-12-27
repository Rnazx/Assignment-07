import library as diff
import math
def f(z,y,x):#The second order differential equation
    return z+1
def g(z,x):#Splitting into two first order equations
    return z
#The function automatically generates a data file which is used to plot the graph
diff.boundary(0,1,1,2*(2.71828-1),5.5,g,f,0.1,0.0001)#The tolerance is 0.0001
diff.boundary(0,1,1,2*(2.71828-1),5.5,g,f,0.01,0.0001)
diff.boundary(0,1,1,2*(2.71828-1),5.5,g,f,0.07,0.0001)
diff.boundary(0,1,1,2*(2.71828-1),5.5,g,f,0.005,0.0001)
#Output
#This code generates a data file. The datapoints are plotted along with the analytical function which is 2*e^x-x-1
#The data file is named "Boundary*insert value of h*.txt" and the plot is named  "Q3_Bound_h=*insert value of h*.pdf"