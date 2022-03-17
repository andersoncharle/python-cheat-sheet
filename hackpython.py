import math
import ipaddress
# new code python
import math

patient_name = 'john doe'
patient_age = 23
old_patient = True
new_patient = False

if not old_patient:
    print("patient name is: " + patient_name)
    print("patient os is: " + str(patient_age))
else:
    print("")


# print message of the user using input function input()
# input("Enter your name: ")
name = ""
if name == "hacker":
    print("your name is: " + name)

    person_name = input("what's your name? ")
    favourite_color = input("What's favorite color? ")
    print(person_name + " likes  " + favourite_color)
    # type of conversion of python
    # int () convert string into integer
    # float() convert string into float
    #  str() convert integer into string

    birthday = (input("Enter your birth year: "))
    age = 2021 - int(birthday)
    print("your current os is: " + str(age))
    # conversion of pound into kilograms
    pounds = input("Enter your weight: ")
    kilogram = float(pounds) * 0.45
    print("your weight are: " + str(kilogram) + "kg")

# Strings cases of using single or double quotes

    double_quotes = "Hi, anderson " \
                "This is our first email to you." \
                "Thank you," \
                "The support team"
    print(double_quotes)

    single_quote = ''' 
Hi, anderson 
This is our first email to you. 
This is our first email to you. 
Thank you, 
The support team

'''
    print(single_quote)
# The index of characters in python can be obtained using square blackets
    example_of_index_of_character = "code with anderson"
    print(example_of_index_of_character[3] + " " + example_of_index_of_character[8] + " " + example_of_index_of_character[17])
#  negative index is the index of the last character (start counting at the last)
    print("using negative index yield: " + example_of_index_of_character[-2])

# for counting range of characters python use colon to count btn range of your characters
    example_of_counting_range = example_of_index_of_character[0:4]
    print("counting range of character using colon yield: " + example_of_counting_range)
#for counting excluded character we use value: or :value
    example_of_counting_excluded_character = example_of_index_of_character[1:-1]
    print("printing excluded character: " + example_of_counting_excluded_character)

# formating string
first_name = 'anderson'
last_name = 'developer'
message = '[' + first_name + ']' + '[' + last_name + ']' + 'is a coder'
msg = f'[{first_name}] [{last_name}] is a coder and hacker'
print(msg)
text_formated = f'{first_name} is software {last_name}'
print(text_formated)

# string method
# length method (len())
coder_name = 'code with anderson and hack with him'
print(len(coder_name))
#To convert all the characters into uperlater we use (.) operator
print("converting into uperlater: " + coder_name.upper())
print("converting into lowecase: " + coder_name.lower())
print("converting into capital later: " + coder_name.capitalize())
print("find() used to find the index of character: " + str(coder_name.find('N')))
print("replace() used to replace text with another: " + coder_name.replace("anderson","hacker"))
is_in_expression = "hack" in coder_name
print("check if hack is in coder_name: " + str(is_in_expression))
print("title() return the title of the string itself: " + coder_name.title())
#arithmetric operation
print("+,-,*,/,//,** are arithmetic operator: " + str(10 ** 3) + " yield of 10 power 3")

# augmented assigment operator +=,-=,*=
x = 10
x = x + 3
print('x = x + 3 is the same as: ' + f'[x+=3] which yield is =' + str(x))

# operator precedence is the same as BODMAS which is the order of operation
# BODMAS stand for (BRACKET,OPERATION,DIVISION,MULTIPLICATION,ADDITON,SUBSTRACTION)
example_of_precedence_or_bodmas = 10 + 3 * 2 ** 2
print(example_of_precedence_or_bodmas)

# MATH FUNCTIONS
y = 3.9
print("round() used to round the decimal digit: " + str(round(y)))
print("absolute stand for abs which return positive number: " + str(abs(-y)))

# module contain  reusable functions for perfoming certain task
# module is the sepate files which contains reusable code
print(math.floor(y))
print(math.factorial(4))

# if statement build program and making decision on some condition
hacker_name = "anderson" in coder_name
if not hacker_name:
    print("find anderson in coder name: " + str(coder_name.find('anderson')))
    print(coder_name.title())
    # print(ipaddress.IPv4Address)
elif hacker_name == True:
    print("else if statement!!!")
else:
    print("nothing to find!!!!")

# examples of if,elif,else statement
price_of_house = 1000000
buyer_has_good_credit = True
if not buyer_has_good_credit:
    print("10% of price of house is: " + str(price_of_house * 0.1) + " of good credit")
elif buyer_has_good_credit == True:
    down_payment = price_of_house * 0.2
    print(f"10% of price of  house is: ${down_payment} of good credit")
    # print("10% of price of house is: " + str(price_of_house * 0.2) + " of good credit")
else:
    print(f"print the payment")

#   LOGICAL OPERATOR
# logical operator such as AND,OR,GREATER THAN OR EQUAL,LESS THAN OR EQUAL,NOT EQUAL
anderson_is_hacker = True
anderson_is_programmer = False
if  anderson_is_hacker and not anderson_is_programmer:
    print(f"anderson is software engineer")
elif anderson_is_hacker or anderson_is_hacker:
    print(f"else if statement say's anderson is mit topper!!!")
else:
    print("return false")

# SIMPLE PROJECT
# weight = int( input("Enter your weight: "))
# select_kilogram = float(weight) * 0.45
# select_pounds = float(weight) / 0.45
# print(input("select either (L)bs or (K)g: "))
# selectL = "l"
# selectK = "k"
# if selectL.lower():
#     print(f"your are {select_pounds} kg")
# elif selectK.lower():
#     print(f"your are {select_kilogram} pounds")
# else:
#     print("nothing to select???")
# print("thank you for using our simple calculator")

# WHILE LOOP used for execute block of code multiple times and build interactive program
#
# while condition:
#     output
# prefix
# declare_i = 1
# while declare_i <=5:
#     print("*" * declare_i)
#     declare_i+=1
#
# # guessing number
# secret_number = 10
# guess_count = 0
# guess_limit = 5
# while guess_count <= guess_limit:
#     guess = int(input("Enter your guessing number: "))
#     guess_count +=1
#     if guess == secret_number:
#         print("You won!")
#         break
#     #     break statement using to terminate the loop
# else:
#      # in python while loop have else statment
#      print("You fail try again!!!")

# CAR GAME
# help = '''
# start - to start the car
# stop - to stop the car
# quit - to exit
# '''
# car = ""
# # car_count = 0
# # car_limit_selection = 4
# # car != "quit"
# while True:
#     car = input(">").lower()
#     car_started = False
#     if car == 'help':
#      print(help)
#     elif car == 'start':
#         if car_started:
#             print("car is already started!")
#         else:
#             car_started = True
#             print("car start..Ready to go!")
#
#     elif car == 'stop':
#         if not car_started:
#             print("car is aleady stopped!")
#         else:
#             car_started = False
#             print("car stopped !!!")
#     elif car == "quit":
#         break
#     else:
#         print("command not found")
#         print("I dont understand that...")

# FOR LOOP used to iterate character in a string
for i in ["code with anderson","nyau","mkakari","rose"]:
    print(i)

for item in range(5,10,2):
    print(item)
prices = [10,20,30]
total = 0
for x in prices:
    total = total + x
print(f"total is: {total}")
for loop in range(3):
    for another in range(3):
        print(f"({loop},{another})")

numbers = [5,2,5,2,2]
for x_count in numbers:
    print("*" * x_count)

# LIST resemble like array
sum_names = 0
for a in ["anderson","fname","lname"]:
    # sum_names = sum_names + a
    print(a[1] + " " + a[0] + a[2])

# dictionary is unordered and mutable collection of items
# dictionary is written with curly brackets
# Each item in dictionary is written in dictionary contain a key/values pair
dictionary_syntax = '''
syntax below show dictionary
dictionary  = {
"key":"values",
"key":"values",
"key":values,
}
'''
print(dictionary_syntax)
person  = {
"firstname":"anderson",
"lastname":"chale",
"os":22,
 "program":"software engineer"
}
print(f"person length is {len(person)}")
print(f"{person}")
# Accessing item,specify the key name of an item inside brackets
person_first = person["firstname"]
person_last = person["lastname"]
person_age = person["os"]
person_pro = person["program"]
print("firstname:",person_first)
print("lastname:",person_last)
print(f"os: {person_age}")
print(f"program: {person['program']}")

# get() method are used also to access the item
print("get() method ",person.get("firstname"))
# Adding item
# T add a new item,specify a new index key name inside
# the square brackets and assign a value using the assigment operator
person["hobby"] = "watching movies and playing football"
add_hobby_to_person_dictionary = person["hobby"]
print(f"my favorite hobbies are {add_hobby_to_person_dictionary}")
# Changing an item Values
person["firstname"] = "code with"
person["lastname"] = "anderson developer"
print(person)

#Removing an item using pop() method by removing the item with a specific key name
person.pop("os")
person.pop("hobby")
print("pop method removing os ",person)
print("pop method removing hobby ",person)

# Another way to remove an item is to use the del keyword
del person["program"]
print(f"removing program using delete keyword:  {person}")
#Getting the length of dictionary using len() method
length_of_dictionary = len(person)
print(f"The length of person dectionary are: {length_of_dictionary} afther renoving some items")
person["python"] = "I love python"
print(person)
#Check if the key exist in the dictionary using in operator
if "I love python" in person:
    print("I love python key exists")
else:
    print("nothing")


# class python_class:
#     __python_object__='''
#     **in python everything is objects**
#     a class help us to create objects
#     use a class keyword to create class
#     syntax:
#     class classname:
#          statement(s)
#     '''
#     first_name=str(input("Enter your first name: "))
#     last_name=str(input("Enter your last name: "))
#     os=int(input("Enter your os: "))
#     print(__python_object__)
# #     instantiating a class
# # now we can create an object to instantiate an object from that class by instantiating it.
# # To instantiate a class,add round brackets () to its class name.
# obj_class=python_class()
# # after instantiating a class we can now access the object's properties
# # access it's properties
# print(f"properties of obj_class after instantiated obj_class=python_class() "
#       f"the output of the firstname be: "
#       f"{obj_class.first_name}")
# print(obj_class.last_name)
# print(obj_class.os)
# python_class

# class attribute
#  A class can have attributes
# For example a student class can have attributes like number_id,name and os
# The __init__() function allow us to provide values for the attributes of a class
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# self parameter allows us to access the attributes and method of a class
# class student:
#     def __init__(self,number_id,name,os):
#         self.number_id = number_id
#         self.name = name
#         self.os = os
# # we can now instantiate it and provide values to it's attributes
# # The process can also be called creating an instance of the class
# # instance is simply object created from a class
#
# student_instance = student(1,"anderson charles",34)
# # After that we can now access the properties of the instance(objects)
# number_id = student_instance.number_id
# name = student_instance.name
# os = student_instance.os
# print(f"number id is: {number_id}, \n"
#       f"student name is: {name}, \n"
#       f"student os is: {os}")
#
# class math:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# instance_ans = math(int(input("Enter value of x: ")),int(input("Enter value of y: ")))
# ans_sum = instance_ans.x + instance_ans.y
# ans_sub = instance_ans.x - instance_ans.y
# ans_mult = instance_ans.x * instance_ans.y
# ans_div = instance_ans.x / instance_ans.y
# print(f"\n\tpython simple calculator of arithmetic operations (BODMAS)\n"
#       f"ans_sub are: {int(ans_sub)}\n"
#       f"ans_sum are: {ans_sum}\n"
#       f"ans_mult are: {ans_mult}\n"
#       f"ans_div are: {float(ans_div)}")

methods = "" \
          "---------" \
          "|||||||||" \
          "====" \
          "methods" \
          "====" \
          "|||||||||" \
          "---------"
print(methods)
# method are functions that can access the class attributes
# These method should be defined(created) inside the class
class student:
    def __init__(self,number_id,name,age):
        self.number_id = number_id
        self.name = name
        self.age = age
    def method_student(self):
        print("***method student***\t>>"
              "Hellow " + self.name + ",how are you?")
student_instance = student(1,"anderson charles",34)
number_id = student_instance.number_id
name = student_instance.name
age = student_instance.age
student_instance.method_student()
print(f"number id is: {number_id}, \n"
      f"student name is: {name}, \n"
      f"student os is: {age}")

# Inheritance
# inheritance is the feature that allow us to create(define) a
# class that inherits the attributes(or properties) and methods of another class.
# for example
class coder_superclass:
    def __init__(self, name, os):
        self.name = name
        self.os = os
    # instantiating a class coder
    def greating_coder(self):
        print("Hellow", self.name)

class scriptkiddies_subclass(coder_superclass):
    def __init__(self, name, os):
        super(scriptkiddies_subclass, self).__init__(name, os)
    def hacker(self):
        print(self.__doc__)
        print("computer name is: ",self.name)
instance_of_inheritance = scriptkiddies_subclass("macintosh","linux")
instance_of_inheritance.greating_coder()
instance_of_inheritance.hacker()
print("os used is: "+instance_of_inheritance.os)

# python formating a string
# we can format a string by adding substrings within it.
# The format() function allows us to format strings.
# PLACEHOLDERS {} helps us to control which parts of the string should be formatted
# they are defined(created) using curly braces {}
let_x = "I love {} very much!"
text = let_x.format("python")
print(text)
x= "The color of {fruits} is {color}"
text = x.format(fruits="banana",color="yellow")
print(text)

# modules
