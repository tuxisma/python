lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)


player_one = LotteryPlayer("Rolf")
player_one.numbers = (1, 2, 3, 6, 7, 8)
player_two = LotteryPlayer("John")

# print(player_one.numbers == player_two.numbers)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    # a cls is a reference for the class (cls=class)
    @classmethod
    def go_to_school(cls):
        # print("I'm going to {}.".format(self.school))
        print("I'm going to school.")
        # In some cases this is useful, pass the class but if isn't just delete cls and things like that
        # we can use @staticmethod (see, file: classes_objects.py)
        print("I'm a {}".format(cls)) # this line prints: I'm a <class '__main__.Student'>


anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
anna.marks.append(56)
anna.marks.append(12)
# print(anna.average())

# when I invoke a object.method(anna.go_to_school) always send a
# parameter(self), even if the parameter of the method is empty
# look at the method, it doenst have parameter but is going to fail
# due to the method in the class doesn[t has self withit it.:
# def go_to_school():
#     # print("I'm going to {}.".format(self.school))
#     print("I'm going to school.")
# If I run this , throw me the next error: go_to_school() takes 0 positional arguments but
# 1 was given
# to solve this write un top of the method the next instruction:
# @classmethod



#So in this case with @classmethod we can use only the name of the class
Student.go_to_school()


