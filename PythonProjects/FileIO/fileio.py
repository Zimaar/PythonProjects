def print_file(): # prints the file. I need to print it more than once so I create a function to prevent repeated code
    new_file = open("new_file.txt")
    lines = new_file.readlines()
    for line in lines:
        print(line)
    new_file.close()

with open("new_file.txt","w+") as new_file: #creating a file called new_file.txt and opening it in write mode
    new_file.write("dog\n")
    new_file.write("can\n")
    new_file.write("parrot\n")
    new_file.write("hamster\n")
    new_file.write("mouse\n")               #writing a list of animals to fill the empty txt file

print_file()

with open("new_file.txt","r") as new_file:
    data = new_file.read() 
    reversed_data = data[::-1] #reading the contents to a variable, and reversing the contents via string splicing

with open("new_file.txt","w") as new_file: #writes the reversed contents back into new_file
    new_file.writelines(reversed_data)
    new_file.close()

print_file()



    
