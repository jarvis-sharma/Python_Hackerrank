# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
a=int(input())
b=int(input())
c=a/b
d=math.atan(c)
print(str(int(round(math.degrees(d))))+'°')
