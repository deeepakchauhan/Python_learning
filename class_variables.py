# CLASS VARIABLES : 
# allows you to share data among all objects created from that class.
# shared among all instances(objects) of a class.
# defined outside the constructor.
# and instance variables are inside the constructor 


class Student:

    Class_year = 2029                                  # class variable, can be accessed through any student 
    num_of_students = 0


    def __init__(self, name, surname, age):
        self.name = name                               # Instance variable 
        self.surname = surname 
        self.age = age 
        Student.num_of_students += 1


student1 = Student("deepak", "chauhan", 20)           # calling the constructor for student 
student2 = Student("yuvraj", "chauhan", 7)


print(Student.num_of_students)   #2
print(student1.name)
print(student2.name)
print(student1.surname)
print(student1.Class_year)
print(student2.Class_year) 

print(f"{student1.name} {student1.surname}'s graduating year is {student1.Class_year}")


        