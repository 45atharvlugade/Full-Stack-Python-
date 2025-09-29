

# ---------------------> Inner List or Nested List<---------------------------------
import random

nested_list = []

for i in range(10):  # Outer list (10 rows)
    inner_list = []
    for j in range(10):  # Inner list (10 columns)
        inner_list.append(random.randint(1, 100))
    nested_list.append(inner_list)

#print(nested_list)

# output --====>
# [[65, 48, 82, 42, 18, 16, 80, 41, 44, 95],
# [26, 20, 62, 15, 18, 70, 58, 31, 52, 90],
# [12, 87, 9, 52, 44, 81, 70, 29, 32, 64],
# [22, 87, 96, 51, 18, 32, 25, 60, 100, 73],
# [88, 98, 74, 87, 42, 60, 46, 42, 50, 92],
# [50, 53, 77, 50, 49, 83, 81, 78, 72, 21],
# [99, 1, 89, 77, 31, 65, 67, 92, 19, 84],
# [54, 100, 50, 81, 38, 38, 75, 95, 50, 77],
# [76, 64, 76, 73, 60, 41, 99, 9, 33, 33],
# [94, 82, 10, 15, 41, 70, 79, 94, 50, 89]]

# Accessing the Elements from the Nested List

# just follow slicing (indexing)
print(nested_list[1][2])
print(nested_list[1][::3])



