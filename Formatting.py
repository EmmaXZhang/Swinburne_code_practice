# print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))
# print('{0:10d})'.format(-123))

# print('{0:<10.2f})'.format(3.14159265))

# print('{0:>10.2f})'.format(3.14159265))

# print('{0:5.2f}'.format(3.14159265))

# print('{0:5d}'.format(12))

# print("Geeks: " + "{0:2d}".format(12),end="")

# print("{0:8.2f}".format(0.545))

#Q1
# input = input("Enter value: ")
#
# if input.isnumeric():
#     input_value = int(input)
#     if 20 < input_value < 30):
#         print("valid")
#     else:
#         print("invalid")
# else:
#     print("invalid")


#Q2
# input_value = input("Enter 4 digit code: ")
# if input_value.isnumeric() and len(input_value) == 4:
#     print("Valid")
# else:
#     print("Invalid")


#Q3
# value = [3.12623,2.718281828,27845.23,145.72]
# i = 0
# while (i < len(value)):
#     print(f"{value[i]:.3f}")
#     i +=1

  # print('{0:.3f}'.format(value[i]))


#Q4
# people_info = {"Bob Liang": 29, "Angelina Zg": 19, "Jane Taksanimia": 25, "Toby Mahammud": 35}
# people_items = list(people_info.items())
#
# i = 0
# while(i < len(people_items)):
#     name,age = people_items[i]
#     print(f"{name:<15}{age:>4}")
#     i+=1
#
# people_info = {"Bob Liang": 29, "Angelina Zg": 19, "Jane Taksanimia": 25, "Toby Mahammud": 35}
#
# for name, age in people_info.items():
#     print(f"{name:<15}{age:>4}")



#Q5
# header = ["mpg", "cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"]
# rows = [
#     ["Mazda RX4", 21.0, 6, 160.0, 110, 3.90, 2.620, 16.46, 0, 1, 4, 4],
#     ["Mazda RX4 Wag", 21.0, 6, 160.0, 110, 3.90, 2.875, 17.02, 0, 1, 4, 4],
#     ["Datsun 710", 22.8, 4, 108.0, 93, 3.85, 2.320, 18.61, 1, 1, 4, 1],
#     ["Hornet 4 Drive", 21.4, 6, 258.0, 110, 3.08, 3.215, 19.44, 1, 0, 3, 1],
#     ["Hornet Sportabout", 18.7, 8, 360.0, 175, 3.15, 3.440, 17.02, 0, 0, 3, 2],
#     ["Valiant", 18.1, 6, 225.0, 105, 2.76, 3.460, 20.22, 1, 0, 3, 1]
# ]

# header formatting
# print('{0:>18s}{1:>4s}{2:>6s}{3:>4s}{4:>5s}{5:>6s}{6:>6s}{7:>3s}{8:>3s}{9:>5s}{10:>5s}'.format("mpg","cyl","disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"))

# # Header formatting
# header_format = '{:>21s}{:>4s}{:>6s}{:>4s}{:>6s}{:>6s}{:>6s}{:>4s}{:>4s}{:>6s}{:>6s}'
# row_format = '{:<13s}{:>6.1f}{:>4.0f}{:>6f}{:>4.0f}{:>5.2f}{:>6.2f}{:>6.2f}{:>3.0f}{:>3.0f}{:>5.0f}'
#
# print(header_format.format(*header))
#
# # Row formatting
# for row in rows:
#     print(row_format.format(*row))



"""
                     mpg cyl  disp  hp drat    wt  qsec vs am gear carb

Hornet Sportabout   18.7   8 360.0 175 3.15 3.440 17.02  0  0    3    2

Valiant             18.1   6 225.0 105 2.76 3.460 20.22  1  0    3    1

"""

# car1_nm = "Hornet Sprotabout"
#
# car1_mpg = 18.7
#
# car1_cyl = 8
#
# car1_disp = 360.0
#
# car1_hp = 175
#
# car1_drat = 3.15
#
# car1_wt = 3.440
#
# car1_qsec = 17.02
#
# car1_vs = 0
#
# car1_am = 0
#
# car1_gear = 3
#
# car1_carb = 2
#
# # Header
#
# print("                    mpg cyl  disp  hp drat    wt  qsec vs am gear carb")
#
# print("{0:19s}".format(car1_nm),end="")
#
# print("{0:4.1f}".format(car1_mpg),end="")
#
# print("{0:4d}".format(car1_cyl),end="")
#
# print("{0:6.1f}".format(car1_disp),end="")
#
# print("{0:4d}".format(car1_hp),end="")
#
# print("{0:5.2f}".format(car1_drat),end="")
#
# print("{0:6.3f}".format(car1_wt),end="")
#
# print("{0:6.2f}".format(car1_qsec),end="")
#
# print("{0:3d}".format(car1_vs),end="")
#
# print("{0:3d}".format(car1_am),end="")
#
# print("{0:5d}".format(car1_gear),end="")
#
# print("{0:5d}".format(car1_carb),end="")

#Q6

pi2 = 3.141592654

max_decimal = 9
i=1
print(f"{'3.':>{max_decimal + 1}}")
while i < max_decimal:
    print(f"{pi2:>{max_decimal+1}.{i}f}")
    i+=1
