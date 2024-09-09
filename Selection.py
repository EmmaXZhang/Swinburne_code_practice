# #Q 1
# age = int(input("what is your age: "))
# if age > 17:
#     print("Legally adult age")
# else:
#     print("Legally not adult age")
#
# #Q2
# gender = input("what is your gender M/F? ")
# age = int(input("what is your age? "))
#
# if age > 17:
#     print(f"{gender} is an adult")
# else:
#     print(f"{gender} is not an adult")


# Q3
# num1 = int(input("number 1: "))
# num2 = int(input("number 2: "))
# num_total = num1 + num2
# if num_total > 10:
#     print("Sum of numbers is greater than 10")
# elif num_total < 10:
#     print("Sum of numbers is less than 10")
# else:
#     print("Sum of numbers is equal to 10")


# Q4
# num = int(input("Please type a number: "))
# if num % 2 == 1:
#     print(f"{num} is odd")
# else:
#     print(f"{num} is even")

#Q1
# value = [66, 43, 1, 6, 2, 99, 4]
# for num in value:
#     if num < 10:
#         print(f"{num}")

#Q2
# t1 = input("Enter the date in the form dd/mm/yyyy: ")
# date = t1.split("/")
#
# print(f"Day:{date[0]}")
# print(f"Month:{date[1]}")
# print(f"Year:{date[2]}")

#Q3
values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
total = 0
i = 0
max_num = values[0]

while (i < len(values)):
    total = total + values[i]
    if values[i] > max_num:
        max_num = values[i]
    i+=1

average = total / len(values)
print(f"Total is {total}, Average is {average}. Largest number is {max_num} ")

# for num in values:
#     total = total + num