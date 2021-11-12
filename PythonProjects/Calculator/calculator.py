import time

while(True):
    print("Calculator App")
    choice = input("Select your mode of operation:\nA: Addition\nB: Subtraction\nC: Multiplication\nD: Division\nor enter 'E' to exit: ")
    
    choice = choice.upper().strip()
    
    if choice in ('A', 'B', 'C', 'D'):
        int_a = float(input("Input the first number: "))
        int_b = float(input("Input the second number: "))

        if choice == 'A':
            print(f"{int_a} + {int_b} = {int_a + int_b}")
            time.sleep(1)

        elif choice == 'B':
            print(f"{int_a} - {int_b} = {int_a - int_b}")
            time.sleep(1)

        elif choice == 'C':
            print(f"{int_a} * {int_b} = {int_a * int_b}")
            time.sleep(1)

        elif choice == 'D':
            print(f"{int_a} / {int_b} = {round(int_a / int_b,5)}")
            time.sleep(1)

    elif choice == 'E':
        exit()
        
    else:
        print("Invalid Input. Select A, B, C or D")

