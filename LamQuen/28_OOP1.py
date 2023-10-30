class SimpleClass2:
    def __init__(self) :
        self.name = "Duy"

    #phuong thuc methods
    def hello(seft):
        print("Hello "+seft.name)

    #static methods
    def hi(name):
        print("Hi " +name)

a = SimpleClass2()
b = SimpleClass2()

a.hello()

SimpleClass2.hi("Anh Duy")


