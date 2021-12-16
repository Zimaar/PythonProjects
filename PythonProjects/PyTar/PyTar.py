import tarfile
import os.path

count = int(input("How many files would you like to compress in one tar.gz: "))
file_name = input("Enter compressed tar.gz filename: ")
file_name = file_name + ".tar.gz"

with tarfile.open(file_name, "w:gz") as tar:
    for x in range(count):
        tar.add(input("Enter filename: "))
    tar.close()
