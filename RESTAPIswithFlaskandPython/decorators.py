# a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
import functools
#DECORATOR WITHOUT ARGUMENTS
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("after the decorator")
    return function_that_runs_func


@my_decorator
def my_function():
    print("I'm the function!")

#my_function()

#we can use decorator if you can to give permissions to an admin page, we can pass the user permissions
#decorator with arguments use it for insert daatas to an Database if can math for a criteria
#we can just show some contents to some user

#DECORATOR WITH ARGUMENTS
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator!")
            if number == 56:
                print("Not running the function!")
            else:
                func(*args, **kwargs)
            print("After the decorator")
        return function_that_runs_func
    return my_decorator

#complex decorator: can accept arguments itself
@decorator_with_arguments(56)
def my_function_too(x, y):
    print(x + y)

my_function_too(57, 67)

