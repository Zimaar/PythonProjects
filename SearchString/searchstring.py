with open("sample.txt",'r') as f:
    string = input("What country are you looking for? ") # asks for user input
    string = string.lower() # makes input lowercase, since txt is all lowercase
    count = 0 # starts a counter to print line #

    for line in f:
        line = line.rstrip() # removes all traling characters
        count += 1

        if string == line:
            print("Found " + line + " at line #" + str(count))
            break # breaks if country is found
    else:
        print("Invalid Input") # exception if user entered incorrectly
