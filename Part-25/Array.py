# Array in Python
# Array is a data structure
# array is a way of organizing data

import numpy as np
import array

# basic array using List

arr = [1, 2, 3, 4, 5]
print(arr[0])  # Output: 1 (index 0 = 1)
arr.append(6)
print(arr)     # Output: [1, 2, 3, 4, 5, 6]

# By using Array Module

arr = array.array('i', [1, 2, 3, 4])
arr.append(5)
print(arr)  # array('i', [1, 2, 3, 4, 5])


# Numpy array

arr = np.array([1, 2, 3, 4])
print(arr * 2)      # [2 4 6 8]
print(arr.mean())   # 2.5

