with open("sample.txt",'r') as f:
    string = "Pakistan"
    for line in f:
        line = line.rstrip()
        if string == line:
            print(line)
            break
