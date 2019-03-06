#Because of the first-class nature of functions in Python, you can define functions inside other functions.
# Such functions are called nested functions.

def parent():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing form the first_child() function."
    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())


