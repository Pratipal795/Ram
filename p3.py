"""Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8 Then, the output should be:40320"""

x=[1,2,3,4,5,6,7,8,9,10]

def inc(x):
    i=1
    while x>0:
        i=i*x
        x-=1
    return i
r=list(map(inc,x))
print(r)
