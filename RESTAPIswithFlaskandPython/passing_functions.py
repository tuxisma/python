#Passing functions a parameters
def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

#You can look here that we are calling methodception, passing as parameter the add_two_numbers function
#without use: () , so the methodfunction call add_two_numbers then the method called(add_two_numbers)
#return the sum result

#print(methodception(add_two_numbers))



#Here we can create a lambda(an anonymous function):
#lambda don have a name, must of the time is writen in one line
#print(methodception(lambda: 35 + 77))



#when we have many data, we can manipulate with filter build function
#if you use 'filter', you must use 'list' if you want it to come out in the form of a list
my_list = [13, 56, 77, 484]

#print(list(filter(lambda x: x != 13, my_list)))



#this lambda function does the same as a normal function that you can see below

#lambda
#(lambda x: x * 3) (5)

#function does the same as lambda
#def f(x):
 #   return x * 3

#f(5)



#we can create a function to filter data also then use filter
#filter is neat and essentially goes against list comprehension

def not_thirteen(x):
    return x != 13

print(list(filter(not_thirteen, my_list)))


#doing the same with list comprehension
#Many python programers would rather use list comprehension, but if you work with other programers
#that use other languages , use filter, because in other language is weird to see list comprehension
print([x for x in my_list if x != 13])




