"""Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use init method to construct some parameters"""

class Ram:
    def __init__(self,s1):
        self.s1=s1
    def getstring(self):
        self.s1=input("enter any string")
    def printstring(self):
        self.s1=self.s1.upper()
        print(self.s1)
r=Ram("ram")
r.getstring()
r.printstring()
