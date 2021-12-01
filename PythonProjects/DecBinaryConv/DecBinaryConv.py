def DecToBinary(num):
    return (bin(num).replace("0b","")) #returning converted binary num, newline at end

def BinaryToDec(binary):
    return int(binary,2)

while True:
    print("Decimal | Binary Converter")
    choice = input(" Select 1 for Decimal To Binary Conversion\n Select 2 for Binary to Decimal Conversion\n Select 3 to Exit\n").strip()

    if choice == '1':
        num = input("Enter the decimal to convert: ")
        print(f"This is your number in decimal: {num}")
        print("This is your number in binary: ", DecToBinary(int(num)))
    
    if choice == '2':
        binary = input("Enter the binary to convert: ")
        print(f"This is your number in binary: {binary}")
        print("This is your number in decimal: ", BinaryToDec(binary))
    
    if choice == '3':
        break

    else:
        print("Invalid Input, enter 1, 2 or 3")
