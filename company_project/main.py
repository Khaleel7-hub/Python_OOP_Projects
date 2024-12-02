class Employee:
    def __init__(self, name, employee_id, position, salary):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.manager = None  # Reference to the manager (if any)

    def calculate_bonus(self):
        return self.salary * 0.05

    def get_details(self):
        return (
            f"Employee Details:\n"
            f"Name: {self.name}\n"
            f"Employee ID: {self.employee_id}\n"
            f"Position: {self.position}\n"
            f"Salary: {self.salary}\n"
        )


class Manager(Employee):
    def __init__(self, name, employee_id, position, salary):
        super().__init__(name, employee_id, position, salary)
        self.subordinates = []  # List of employees under this manager

    def calculate_bonus(self):
        # 5% of own salary + 1% of the total salaries of subordinates
        subordinate_salaries = sum(emp.salary for emp in self.subordinates)
        return super().calculate_bonus() + (0.01 * subordinate_salaries)

    def add_subordinate(self, employee):
        self.subordinates.append(employee)
        employee.manager = self

    def remove_subordinate(self, employee):
        if employee in self.subordinates:
            self.subordinates.remove(employee)
            employee.manager = None

    def get_details(self):
        subordinate_details = "\n".join(
            [f"{sub.name} ({sub.position})" for sub in self.subordinates]
        ) or "No subordinates"
        return (
            super().get_details()
            + f"Subordinates:\n{subordinate_details}\n"
        )
     def func (self):
          return len (self.subordinates)
# Task Class
class Task:
    def __init__(self, task_id, description, status="Pending"):
        self.task_id = task_id
        self.description = description
        self.status = status

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Status: {self.status}"

# Address Class
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def full_address(self):
        return f"{self.city}, {self.state}"

# Department Class
class Department:
    def __init__(self, name):
        self.name = name
        self.manager = None

    def assign_manager(self, manager):

        self.manager = manager

    def __str__(self):
        manager_name = self.manager.name if self.manager else "No manager assigned"
        return f"Department: {self.name}, Manager: {manager_name}"

class Company:
    def __init__(self, name):
        self.name = name
        self.general_manager = None  # Reference to the highest-level manager
        self.employees = {}  # Dictionary to store all employees by their ID

    def add_employee(self, employee, manager_id=None):
        if manager_id is None:
            # Assign general manager
            if self.general_manager is None:
                self.general_manager = employee
            else:
                raise ValueError("General manager already assigned.")
        else:
            # Add employee under a specific manager
            manager = self.find_employee_by_id(manager_id)
            if isinstance(manager, Manager):
                manager.add_subordinate(employee)
            else:
                raise ValueError("Manager not found or invalid.")
        self.employees[employee.employee_id] = employee

    def find_employee_by_id(self, employee_id):
        return self.employees.get(employee_id, None)

    def list_employees(self):
        if not self.general_manager:
            print("No employees to display.")
            return

        print(f"Company: {self.name}")
        print("Employees (BFS Order):")
        
        queue = [self.general_manager]  # Start BFS from the general manager
        while queue:
            current = queue.pop(0)  # Remove the current employee/manager from the queue
            print(current.get_details())  # Display their details
            
            # If the current person is a manager, add their subordinates to the queue
            if isinstance(current, Manager):
                queue.extend(current.subordinates)

    def calculate_company_salary(self):
        return sum(emp.salary for emp in self.employees.values())

    def func(self):
        return len (list_emploeeys)
