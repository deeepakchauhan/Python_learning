#                                  CLASS METHODS : 
# Allow operations related to the class itself
# takes (cls) as the first parameter, which represents th class itself
# @classmethod : That means it can access/modify class-level data,

class Student:
    college_name = "SVNIT"                       # class variable, shared by all the objects 

    def __init__(self, name , gpa):
        self.name = name 
        self.gpa = gpa


        @classmethod                            # the function below is a class method, not an instance method 
        
        def change_college(cls, new_college):    # cls refers to the class itself (student)
            cls.college_name = new_college

        
        def Show(self):
            print(f"Name: {self.name}, GPA: {self.gpa}, College: {Student.college_name}") 




s1 = Student("deepak", 3.5)
s1.Show()  
