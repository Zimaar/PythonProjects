import socket

url  = input("Enter the URL of the website: ").strip().lower() #getting URL from user input and removing whitespace/lowercasing

ip_address = socket.gethostbyname(url) #getting IP Address through hostname

print("URL: " + url)
print("IP Address: " + ip_address)
