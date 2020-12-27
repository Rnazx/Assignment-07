import library as diff
import math
def f1(y,x):#Q1a
    return (y*math.log(y))/x
def f2(y,x):#Q1b
    return 6-((2*y)/x)
#The functions automatically generates a data file which is used to plot the graph
#Question a
diff.euler(2,2.71828,f1,0.5,10)#range from 2 to 10
diff.euler(2,2.71828,f1,0.1,10)
diff.euler(2,2.71828,f1,0.05,10)
diff.euler(2,2.71828,f1,0.01,10)
#This code generates a data file. The datapoints are plotted along with the analytical function which is e^(x/2)
#The data file is named "Euler*insert value of h*.txt" and the plot is named  "Q1a_Euler_h=*insert value of h*.pdf"
#Question b
diff.euler(3,1,f2,0.52,10)#range from 3 to 10
diff.euler(3,1,f2,0.12,10)
diff.euler(3,1,f2,0.052,10)
diff.euler(3,1,f2,0.012,10)
#This code generates a data file. The datapoints are plotted along with the analytical function which is 2x-45/(x^2)
#The data file is named "Euler*insert value of h*.txt" and the plot is named  "Q1b_Euler_h=*insert value of h*.pdf"

#Output
#This code generates a data file. The datapoints are plotted along with the analytical function 
