with open("sample.txt",'r') as f:
    string = input("What country are you looking for? ")
    string = string.strip().capitalize()
    count = 0

    for line in f:
        line = line.rstrip()
        count += 1

        if string == line:
            print("Found " + line + " at line #" + str(count))
            break
    else:
        print("Invalid Input")
