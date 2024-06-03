'''Takes an inputted phrase and encodes it using a given hashing method'''
import hashlib

# Input a password
password = input("Enter a password: ")

#Hash with MD5
MD5 = hashlib.md5(password.encode()).hexdigest()
#Print MD5 hash
print("MD5: ", MD5)

#Hash with SHA-256
SHA_256 = hashlib.sha256(password.encode()).hexdigest()
#Print SHA-256 Hash
print("SHA-256: ", SHA_256)

#Hash with SHA-512
SHA_512 = hashlib.sha512(password.encode()).hexdigest()
#Print SHA-512 Hash
print("SHA-512: ", SHA_512)
