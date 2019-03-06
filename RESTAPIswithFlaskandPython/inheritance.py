class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        # return a new student called 'friend_name' in the same school as self.
        # args = 17.50, **kwargs = job_title="software developer"
        return cls(friend_name, origin.school, *args, **kwargs)


class WorkingStudent(Student):
    # Here I'm inhering the super class with a extra attribute(salary)
    def __init__(self, name, school, salary, job_title):
        # These properties are from Student class but necessary to use them here due to the inheritance.
        super().__init__(name, school)
        # The extra properties, the rest of the properties are from Student Class(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent("Anna", "Oxford", 20.00, "Software Developer")
print(anna.salary)


friend = WorkingStudent.friend(anna, "Greg", 17.50, job_title="software developer")
print(friend.name)
print(friend.school)
print(friend.salary)
print(friend.job_title)
