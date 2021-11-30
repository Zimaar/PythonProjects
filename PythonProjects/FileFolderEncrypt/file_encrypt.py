from cryptography.fernet import Fernet
#Method to encrypt file
def encrypt(filename, key):
    f = Fernet(key) #creating private key with Fernet

    with open(filename, "rb") as file:
        file_data = file.read() #reading file contents

    encrypted_data = f.encrypt(file_data) #encrypting file

    with open(filename, "wb") as file:
        file.write(encrypted_data) #writing encrypted data to new file

#Method to decrypt files
def decrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read() # reading encrypted file

    decrypted_data = f.decrypt(encrypted_data) #decrypting data with key

    with open(filename, "wb") as file:
        file.write(decrypted_data) #rewriting decrypted data



key = Fernet.generate_key()
file = 'data1.csv'
encrypt(file, key) #calling encrypt method

decrypt(file, key) #decrypting file
