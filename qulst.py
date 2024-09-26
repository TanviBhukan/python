t = []

def Insert():
    """Insert an element into the queue."""
    if len(t) == size:  # Check whether the queue is full
        print("Queue is Full!!!!")
    else:
        element = input("Enter the element: ")
        t.append(element)  # Add the element to the end of the queue
        print(element, "is added to the Queue!")

def Delete():
    """Remove an element from the front of the queue."""
    if len(t) == 0:  # Check whether the queue is empty
        print("Queue is Empty!!!")
    else:
        e = t.pop(0)  # remove the first element from the queue
        print("Element removed!!:", e)

def display():
    """Display the current elements in the queue."""
    print("Current Queue:", t)

# Main body
size = int(input("Enter the size of the Queue: "))  # get the maximum size of the queue

while True:
    # Menu for user operations
    print("\nSelect the Operation: 1.Insert 2.Delete 3.Display 4.Quit")
    choice = int(input())
    
    if choice == 1:
        Insert()  # call insert function
    elif choice == 2:
        Delete()  # call delete function
    elif choice == 3:
        display()  # call display function
    elif choice == 4:
        print("Exiting the program.")
        break  # exit the loop to quit the program
    else:
        print("Invalid Option!!!")  # handle invalid choices
