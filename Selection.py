#Q 1
age = int(input("what is your age: "))
if age > 17:
    print("Legally adult age")
else:
    print("Legally not adult age")

# BEGIN
# PROMPT "what is your age: "
# READ age
# CONVERT age TO INTEGER
# IF  age > 17 THEN
# PRINT "Legally adult age"
# ELSE
# PRINT "Legally not adult age"
# ENDIF
# END

#Q2
gender = input("what is your gender? ")
age = int(input("what is your age? "))

if age > 17:
    print(f"{gender} is an adult")
else:
    print(f"{gender} is not an adult")


# Q3
num1 = int(input("number 1: "))
num2 = int(input("number 2: "))
num_total = num1 + num2
if num_total > 10:
    print("Sum of numbers is greater than 10")
elif num_total <10:
    print("Sum of numbers is less than 10")
else:
    print("Sum of numbers is equal to 10")


# Q4
num = int(input("Please type a number: "))
if num % 2 == 1:
    print(f"{num} is odd")
else:
    print(f"{num} is even")
