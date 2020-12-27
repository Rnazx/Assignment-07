import library as diff
import math
def f(z,y,x):#differential equation
    return 1-x-z
def g(z,x):
    return z
diff.rungekutta4(0,2,1,g,f,0.1,-5,5)#range -5 to 5
diff.rungekutta4(0,2,1,g,f,0.5,-5,5)
diff.rungekutta4(0,2,1,g,f,0.02,-5,5)
diff.rungekutta4(0,2,1,g,f,0.07,-5,5)
#output
#This code generates a data file. The datapoints are plotted along with the analytical function which is 1+exp(-x)-(x^2)/2+2*x
#The data file is named "RK4*insert value of h*.txt" and the plot is named  "Q2_Rk4_h=*insert value of h*.pdf".

