# this example help us to simplify inheritance.py
# *args can receive many values dynamically as **kwargs as well
# the only difference is, kwargs receive values as a key:value
# note that you have to use key:value when you are using double *, example: **kwargs


def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


what_are_kwargs(12, 23, 232, name='Ismael', location='MX')

