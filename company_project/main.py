#Creating Employee Class:
class Employee:
    def __init__ (self, name, employee_id, position, salary): #Creating Attributes
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
    
    def get__details(self): #Display employee details.

    def salary_raise(self): #Increases the employee’s salary by the specified percentage.
        
#Creating Manager Class:
class Manager:
    def __init__ (self, name, employee_id, position, salary, subordinates): #Creating Attributes
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.subordinates = subordinates

    def add_subordiante(self): #Add a subordinate to the manager's team.

    def remove_subordinate(self): #Remove a subordinate from the manager's team.

    def get_subordinates(self): #List the subordinates reporting to the manager.

    def get_details(self): #Display manager details and the list of his/her subordinates.

    def salary_raise(self): #Increases the manger's salary by the sepcified percentage.

class Company:
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees

    def add_employee(self): #Add an employee to the company's list.

    def list_employees(self): #List all employees in the company.
