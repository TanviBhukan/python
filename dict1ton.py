squares_dict = {}

n = int(input("How many numbers do you want to add to the dictionary= "))

for x in range(1, n + 1):
    squares_dict[x] = x * x

print(squares_dict)
