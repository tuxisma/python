class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displaycount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayemployee(self):
        print("Name: ", self.name,", Salary: ", self.salary)

def main():

    # Creating instance of Employee class
    # You can pass arguments that __init__ method accepts
    # Here we are creating instance object
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)

    # Accessing attributes
    # In order to access an attribute you can use dot operator(.) with object
    emp1.displayemployee()
    emp2.displayemployee()
    print("Total Employee %d" % Employee.empCount)

if __name__ == '__main__':
    main()