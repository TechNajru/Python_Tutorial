# ADVANCE ARRAY TOPIC IN NUMPY

import numpy as np

a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
result = a + b
print(result)
# Output:
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]

print("")

arr = np.array([10, 20, 30, 40, 50])
mask = arr > 25
print(arr[mask])  # [30 40 50]

# Fancy indexing
indices = [0, 2, 4]
print(arr[indices])  # [10 30 50]

print("")

a = np.array([1, 2, 3])
b = a.view()
b[0] = 99
print(a)  # [99  2  3] – modifies `a` too!

c = a.copy()
c[1] = 100
print(a)  # Still [99  2  3] – `copy()` keeps original safe

print("")

a = np.arange(12)  # [0, 1, ..., 11]
a = a.reshape(3, 4)
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print("")

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])

# Stacking vertically and horizontally
print(np.vstack([a, b]))  # Vertical stack
print("")
print(np.hstack([a, a]))  # Horizontal stack


print("")

a = np.array([1, 2, 3], dtype=np.int8)
print(a.nbytes)  # Much smaller than default int32/int64
