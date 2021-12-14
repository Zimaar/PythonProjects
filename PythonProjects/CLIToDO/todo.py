import sys
import datetime

#Instruction menu shown to user
def instruction():
    sa = """Usage :-
    ./todo add "todo item" | Add a New ToDo Item
    ./todo ls              | Show remaining todos
    ./todo del NUM         | Delete ToDo Item based on Item ID
    ./todo done NUMBER     | Complete a ToDo based on Item ID
    ./todo help            | Show usage
    ./todo report          | Statistics"""
        sys.stdout.buffer.write(sa.encode('utf8'))

#method for adding item to txt file
def addItem(s):
    f = open('todo.txt', 'a') #opening text files where items are stored
    f.write(s) #writing item to file
    f.write("\n") #line space for readability
    f.close()
    print(f"Added todo: {s} ")

#Printing current todo items
def ls():
    nec()
    l = len(d)
    k = l

    for i in d:
        sys.stdout.buffer.write(f"[{l}] {d[l]}".encode('utf8'))
        sys.stdout.buffer.write("\n".encode('utf8'))
        l = l-1

def done(num):
    nec()
    num = int(num) #converting arguement to int 
    st = 'x '+str(datetime.datetime.today()).split()[0]

    f.write(st)
    f.write("\n")
    f.close()
    print(f"Marked todo #{num} as done.")

    with open("todo.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)

        for i in lines:
            if i.strip('\n') != d[no]:
                f.write(i)
        f.truncate()


    
