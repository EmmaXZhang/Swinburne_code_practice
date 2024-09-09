
# column_name = [row[0], row[1], row[2]]
names = ['bob','lily','liz']

# colum_name = [row[0], row[1], row[2]]
ages = [49,23,12]

'''
names   age
bob     49
lily    23
liz     12
'''

i = 0
n = len(names)
while i < n:
    # left-align,max-width 10, right-align,max-width 5
    print(f"{names[i]:<10}{ages[i]:>5}")
    i=i+1



