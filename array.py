# arr01=[3,8,9]
# arr02 = arr01
# arr01.append(7)
# print(arr01)
# print(arr02)


arr01 = [3, 8, 9]

#arr02 = arr01

# A deep copy - all elements are copied.

arr02 = arr01.copy()

arr01.append(7)



print(arr01)

print(arr02)