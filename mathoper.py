class MathOp:
    def AddOp(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
        self.c = self.a + self.b
        print("Addition is:", self.c)

    def SubOp(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
        self.c = self.a - self.b
        print("Subtraction is:", self.c)

    def MulOp(self):
        self.a = int(input("Enter first number: "))
        self.b = int(input("Enter second number: "))
        self.c = self.a * self.b
        print("Multiplication is:", self.c)

# Main body
obj = MathOp()
while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")
    ch = int(input("Enter choice to perform any operation: "))
    
    if ch == 1:
        obj.AddOp()
    elif ch == 2:
        obj.SubOp()
    elif ch == 3:
        obj.MulOp()
    elif ch == 4:
        print("\nProgram Stopped")
        break
    else:
        print("Wrong Choice")
