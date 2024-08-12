# # Q1
# current_temperature = 0.0
# input_temperature = float(input("Enter a temperature: "))
# if input_temperature > current_temperature:
#     print("not freezing")
# else:
#     print("freezing")


# #Q2
# import random
# secret_num = random.randint(1,11)
# input_num = int(input("Pick an integer from 1 - 10: "))
#
# if input_num == secret_num:
#     print(f"The secret number is {secret_num}. you guess the number correctly")
# else:
#     print(f"The secret number is {secret_num}. you guess the number incorrectly")

# # Q3
# def check_temp(temp):
#     if temp > 30:
#         return print("The porridge is too hot")
#     elif temp < 20:
#         return print("The porridge is too cold")
#     else:
#         return print("The porridge is just right")
#
# current_temp = float(input("What is the porridge temperature?: "))
# check_temp(current_temp)

#Q4

# def check_pwd(input):
#     password = "aBc123"
#     if input == password:
#         print("Valid password")
#     else:
#         print("invalid password")
#
# input_pwd = input("what is your password: ")
# check_pwd(input_pwd)

# #Q5
# def check_password():
#         pwd1 = input("what is your first password: ")
#         if pwd1 == "open":
#             pwd2 = input("what is your second password: ")
#             if pwd2 == "sesame":
#                 print("correct password")
#             else:
#                 print("incorrect password")
#         else:
#             print("incorrect password")
#
# check_password()

#Q6
# def check_num(num):
#     if num in range(1,7):
#         print("input is valid")
#     else:
#         print("input is invalid")
#
# num = int(input("type a number from 1 to 6: "))
# check_num(num)


#Q2
# birth = int(input("what is your year of birth: "))
# age = 2024-birth
# if age >=18:
#     print(f"Your are {age}. Come in and have a drink!")
# else:
#     print("Go away. Child.")

#Q3
name = input("Enter your name: ")
if name.lower() == "frank" or name.lower() == "george":
    print(f"Welcome {name}")
else:
    print("")