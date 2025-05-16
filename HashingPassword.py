import bcrypt

print("Salt 1 - ", bcrypt.gensalt())
print("Salt 2 - ", bcrypt.gensalt())
print("Salt 3 - ", bcrypt.gensalt())
print("Salt 4 - ", bcrypt.gensalt())

mypass = "thisismypassword"
# Hashing the password
mypass = bytes(mypass, "utf-8")
print("Bytes password:", mypass)
string_salt = "my_custom_salt"
#salt = bytes(string_salt, "utf-8")
#salt = bcrypt.hashpw(salt, bcrypt.gensalt())
#salt = bcrypt.gensalt()
salt = b'$2b$12$GlXC3JSuwm.gf/jiQrNJIO'
print(type(salt))
print("Salt : " , salt)
my_hashed_salt = bcrypt.hashpw(mypass, salt)
print("Hashed password with salt:", my_hashed_salt)

#Verifying the password
print("Verifying password...")
input_password = input("Enter your password: ")
byte_password = bytes(input_password, "utf-8")
print("Bytes password:", byte_password)
input_hashed = bcrypt.hashpw(byte_password, salt)
print("Hashed password with salt:", input_hashed)

# Check if the input password matches the hashed password
if my_hashed_salt == input_hashed:
    print("Password is correct")
else:
    print("Password is incorrect")

# Check if the input password matches the hashed password with salt
if bcrypt.checkpw(byte_password, my_hashed_salt):
    print("Password is correct")
else:
    print("Password is incorrect")
