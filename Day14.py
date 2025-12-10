

# Class- 
# 
# is a blueprint of a object
# having state and behavior 
# method and properties


# object- instance of a class ( created from blueprint )

# class- Car
            # company, color,model,brand,features


# object
# car1=Car()
# car2=Car()



# ****************************************************************


# eg

#  Creating a Class

# class Car:
#       pass


# creating object

# car1=Car()
# car2=Car()

# print(car1)
# print(car2)




# ***************************************************


# Adding Attributes (Variables inside class)


class Student:
    student_name="Sumit"
    student_course="Python FUll Stack"
    student_skill="Python"


    # (Functions inside class)

    def studentDetails(self):
        print("students details function called")


stud=Student()
print(stud.student_name)
print(stud.student_course)
print(stud.student_skill)

stud.studentDetails()
