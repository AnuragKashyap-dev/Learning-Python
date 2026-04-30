from random import randint

class Train :
    def __init__(self,trainno):
        self.trainno = trainno

    def book(self, fro , to ):
        print(f"Ticket is booked in train no {self.trainno} from {fro} to {to}")

    def getstatus(self ):
        print(f"Train no :{self.trainno} is running !")

    def getfare(self,fro,to ):
        fare = randint(566,677)
        print(f"Fare from {fro} to {to} is {fare}")


t = Train(12234)
t.book("bmki","bth")       
t.getstatus()       
t.getfare("bmki","bth")       
       
