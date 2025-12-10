
# eg -1

class Car:
    company="Tesla"
    model="Tesla Y"
    color="white"
    range="400 KM"
    HP="200 HP"
    

    def start(self):
        print("car Is Started....")

    def stop(self):
        print("Car is Stopped...")  

    def details(self):
        print(f""" company Is = {self.company} and model {self.model} , color={self.color} """)



# instance ie, object

car1=Car()
car1.start()
car1.stop()
car1.details()

# ******************************************************

# 2

# class Animal:
#     name="Dog"

#     def sleeping(self):
#         print("Animal is sleeping", self.name)

#     def eating(self):
#         print("Animal is eating...😊", self.name)
    
#     def barking(self):
#         print("Animal Is Barking...", self.name)

# animal1=Animal()
# animal1.eating()
# animal1.barking()
# animal1.sleeping()


# **********************************************************

# 3


class Animal:

    def sleeping(self,animal_name):
        print("Animal is sleeping", animal_name)

    def eating(self,animal_name):
        print("Animal is eating...😊", animal_name)
    
    def barking(self,animal_name):
        print("Animal Is Barking...", animal_name)

animal1=Animal()
animal1.eating("Cat")
animal1.barking("Cat")
animal1.sleeping("Cat")