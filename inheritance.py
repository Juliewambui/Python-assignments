from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        pass    

    def calculate_salary(self):
        return f"Employee salary: {self.salary}"
    
    class HourlyEmployee(Employee):
        def __init__(self, emp_id, name, salary, hourly_rate, hours_worked):
            super ().__init__(emp_id, name, salary)
            self.hourly_rate = hourly_rate
            self.hours_worked = hours_worked

        def calculate_salary(self):
            self.salary = self.hourly_rate * self.hours_worked
            return self.salary   
        
        class SalariedEmployee(Employee):
            def __init__(self,emp_id, name, salary, monthly_salary):
                super ().__init__(emp_id, name, salary)
                self.monthly_salary = monthly_salary

            def calculate_salary(self):
                self.salary = self.monthly_salary
                return self.salary

hourly_emp = HourlyEmployee(100, "Julie", 10000, 50, 180)
salaried_emp = SalariedEmployee(101, "James", 20000, 100, 180)

       