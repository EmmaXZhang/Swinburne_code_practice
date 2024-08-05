#Q1
# current_temperature = 25
# input_temperature = int(input("Enter a temperature: "))
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
# def check_password(password):
#     correct_password = "open sesame"
#     if password == correct_password:
#         print("The cave is now open!")
#     else:
#         print("Incorrect password. Try again.")
#
# input_pwd = input("what is your password: ")
# check_password(input_pwd)

#Q6
def check_num(num):
    if num in range(1,7):
        print("input is valid")
    else:
        print("input is invalid")

num = int(input("type a number from 1 to 6: "))
check_num(num)