# Using tuples
a = (1, 2, 3, 4)
b = (4, 5, 6, 7)
c = (2, 2, 3, 8)

print("Original tuples:")
print(a)
print(b)
print(c)

print("\nElement-wise sum of the said tuples:")
result = tuple(map(sum, zip(a, b, c)))
print(result)

# Using NumPy arrays
from numpy import array

list1 = [1, 5, 7]
list2 = [3, 2, 1]

y = array(list1)
z = array(list2)

print("\nElement-wise sum of the said lists (as arrays):")
print(y + z)
