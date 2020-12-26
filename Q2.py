import library as diff
import math
def f(z,y,x):
    return 1-x-z
def g(z,x):
    return z
diff.rungekutta4(0,2,1,g,f,0.1,-5,5)
diff.rungekutta4(0,2,1,g,f,0.5,-5,5)
diff.rungekutta4(0,2,1,g,f,0.02,-5,5)
diff.rungekutta4(0,2,1,g,f,0.07,-5,5)

