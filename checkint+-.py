num = int(input("Enter any positive number: "))

try:
    # Check if the number is positive
    if num < 0:
        raise ValueError("Negative Number - Input Number is Incorrect")
    else:
        print("Positive Number - Input Number is Correct")
except ValueError as t:
    # Catch and print the ValueError message
    print(t)