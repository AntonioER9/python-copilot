class Employee:
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

employee_list = [
  Employee("Alice", 25, 80000),
  Employee("Bob", 30, 100000),
  Employee("Charlie", 35, 120000),
  Employee("David", 40, 140000),
  Employee("Eve", 45, 160000),
  Employee("Frank", 50, 180000),
]

def get_all_employees_names():
  return [employee.name for employee in employee_list]

def get_maximal_salary():
  return max([employee.salary for employee in employee_list])

def get_employees_with_salary_bigger_than(salary):
  return [employee.name for employee in employee_list if employee.salary > salary]

print(get_maximal_salary())

