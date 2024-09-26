check_string = "Main homework nahi karna chahta!"
dict = {}

# Counting occurrence of char
for ch in check_string:
    if ch in dict:
        dict[ch] += 1
    else:
        dict[ch] = 1

# result
for key in dict:
    print(key, "-", dict[key])
