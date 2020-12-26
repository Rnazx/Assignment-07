import library as diff
import math
def f1(y,x):
    return (y*math.log(y))/x
def f2(y,x):
    return 6-((2*y)/x)
#Question 1
diff.euler(2,2.71828,f1,0.5,10)
diff.euler(2,2.71828,f1,0.1,10)
diff.euler(2,2.71828,f1,0.05,10)
diff.euler(2,2.71828,f1,0.01,10)
#Question 2
diff.euler(3,1,f2,0.52,10)
diff.euler(3,1,f2,0.12,10)
diff.euler(3,1,f2,0.052,10)
diff.euler(3,1,f2,0.012,10)

