#Q1
# i=1
# sum=0
# while(i<1001):
#     sum=sum+i
#     i+=1
#
# print(sum)

#Q2
# i = 0
# while i<15:
#     num = i % 10
#     print(num,end="")
#     i+=1

#Q3
# import random
# random_num = random.randint(1,10)

random_num=4
user_input = int(input("Guess number between 1 to 10: "))
while(user_input != random_num):
    if(user_input > random_num):
        print("too high")
        user_input = int(input("Guess number between 1 to 10: "))
    else:
        print("too low")
        user_input = int(input("Guess number between 1 to 10: "))

print("Correct")
