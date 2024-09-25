# Initialize array
t = (6,3,4,5,2, 2, 5, 7, 9, 4, 3)
print(t)
lst = []
print("Repeated elements in the given tuple:")

# Searches for repeated elements
for i in range(len(t)):
    if t.count(t[i]) > 1:
        if t[i] not in lst:
            lst.append(t[i])
            print(t[i])
