def isMonotonic(A):
    increasing = decreasing = True
    for i in range(1, len(A)):
        if A[i] > A[i - 1]:
            decreasing = False
        elif A[i] < A[i - 1]:
            increasing = False
    return increasing or decreasing
A = [6, 5, 4, 4]
# Print 
print(isMonotonic(A))  
