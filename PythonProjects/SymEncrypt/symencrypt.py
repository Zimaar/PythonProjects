from cryptography.fernet import Fernet 

message = input("Enter the message you would like to encrypt: ") #Getting message from user input
key = Fernet.generate_key() #Using fernet to generate encryption key
fernet = Fernet(key) #Instantiating the fernet class with key
enc_message = fernet.encrypt(message.encode()) #creating encrypted message with fernet key

print(f"This is your original message: {message}")
print(f"This is your encrypted message: {enc_message}")
print(f"This is your encryption key: {key}")

fernet = Fernet(key) #Instantiating fernet with user's key
dec_message = fernet.decrypt(enc_message).decode()

print(f"This is your encrypted message: {message}")
print(f"This is your decrypted message: {dec_message}")
        


