class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def show_info(self):
        print(f"{self.name} — {self.position}, зарплата: {self.salary} грн")
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Працівника {employee.name} додано у відділ {self.name}")
    def remove_employee(self, name):
        for emp in self.employees:
            if emp.name == name:
                self.employees.remove(emp)
                print(f"🗑 Працівника {name} видалено з відділу {self.name}")
                return
        print(f"Працівника '{name}' не знайдено у відділі")
    def show_employees(self):
        if not self.employees:
            print(f"У відділі {self.name} поки немає працівників")
        else:
            print(f"Працівники відділу {self.name}:")
            for emp in self.employees:
                emp.show_info()
    def total_salary(self):
        total = sum(emp.salary for emp in self.employees)
        print(f" Загальний фонд зарплат відділу {self.name}: {total} грн")
emp1 = Employee("Олег", "Менеджер", 18000)
emp2 = Employee("Марія", "Бухгалтер", 22000)
emp3 = Employee("Ігор", "Програміст", 30000)
department = Department("Фінансовий відділ")
department.add_employee(emp1)
department.add_employee(emp2)
department.add_employee(emp3)
print()
department.show_employees()
department.remove_employee("Марія")
print()
department.show_employees()
department.total_salary()
