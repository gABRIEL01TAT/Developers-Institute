# def say_hello(username, language):
#     if language == "EN":
#         print("Hello "+username)
#     elif language == "FR":
#         print("Bonjour "+username)
#     else:
#         print("This language is not supported: " + language)

# #say_hello("Rick", "EN")

# say_hello("Rick", language="FR")

# def greet_ings(first_name, languages, age):
#     if languages == "GER":
#         print("Guten Morgren"+first_name+""+languages+ age)
#     elif languages == "EN":
#         print("good morning"+first_name+""+languages+""+"You are"+age)
#     # elif languages == "FR":
#     #       print("Bonjour "+first_name+""+"comment ca va"+""+age)
#     else:
#         print("The language is unknown")



# def divide_by_three(number):
#   return number / 3

# first_number = 20000
# first_number_computed = divide_by_three(first_number)
# print(first_number_computed)


# second_number = 27
# second_number_computed = divide_by_three(second_number)
# print(second_number_computed)


def calculation(a, b):
    return ("the addition is {} and the subtraction is {}".format((a+b),(a-b)))
a = int(input("enter a number "))
b = int(input("enter a number "))

res = calculation(a, b)
print(res)