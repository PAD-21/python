class Animal:
    def __init__(self,animalTypeA, nameA, widthA, heightA, weightA):
        self.animalType= animalTypeA
        self.name = nameA
        self.width= widthA
        self.height = heightA
        self.weight = weightA

    
        
    #phat ra am thanh
    def makeVoice(self):
        print("Unknow voice")

    #in thông tin
    def printMe(self):
        print("animalType:{0},name ={1},width = {2} , heigh={3},weight={4}".format(self.animalType , self.name,self.width, self.height, self.weight))

a1= Animal("con nguoi","Duy","","170cm","54kg")
a1.printMe()
a1.makeVoice()

class Dog(Animal):
    def __init__(self,nameA, widthA, heightA,weightA, isChampionA):
       Animal.__init__(self,"Dog",nameA,widthA,heightA,weightA)
       self.isChampion = isChampionA
    
    #override method
    def makeVoice(self):
        print("{0}: gau gau ".format(self.name))

    
dog1=Dog("cậu vàng","145cm","50cm","54kg",True)
dog1.makeVoice()
dog1.printMe()



