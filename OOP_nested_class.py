# NESTED CLASS :
 
# Class defined within another class 
# Allows you to logically group classes that are closely related 
# Encapsulates private details that aren't relevent outside the outer class.
# Reduces the possibilities of naming conflict, and also keeps the namespace clean


class Company:
    class Employee():
        def __init__(self, name, position):
            self.name = name
            self.position = position 

        def get_details(self):
            return f"{self.name}  {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name

        self.employees = []                                      # we will use method to add employees to this list

    
    def add_employee(self, name, position):
        new_employee = self.Employee(name, position) 
        self.employees.append(new_employee)


    def list_employees(self):
        return [ employee.get_details() for employee in self.employees ]

company1 = Company("Google")
company2 = Company("F1")

company1.add_employee("Deepak Chauhan", "Manager")
company1.add_employee("Yuvraj Chauhan", "Project Manager")
company1.add_employee("Anurag Chauhan", "Product Manager")

company2.add_employee("Lewis Hamilton", "Scuderia Ferrari")
company2.add_employee("Max Verstappen", "Mercedes")
company2.add_employee("Oscar Piastri", "McLaren")





# print(company.list_employees()) 

for employee in company1.list_employees():
    print(employee)

print()

for employee in company2.list_employees():
    print(employee)    
