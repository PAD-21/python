class SimpleClass:
    #Attribute
    i=5

    #_init_
    def __init__(self):
        self.j=7

    #methods
    def printMe(self):
        print(self.j)

objectA = SimpleClass()
objectB = SimpleClass()

objectA.printMe()
print(objectB.i)

#thay doi gia tri thuoc tinh
objectA.i =100
objectB.j =500
print(objectA.i)
objectB.printMe()