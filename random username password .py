import random
import string
import secrets

# -------- Username Generator --------
name = input("Enter your name: ")

num = random.randint(100, 999)   # random number
username = name.lower() + str(num)

# -------- Password Generator --------
length = 12

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(characters) for _ in range(length))

# -------- Output --------
print("\nAccount Created Successfully!")
print("Username:", username)
print("Password:", password)

#output
Enter your name: akhil
Account Created Successfully!
Username: akhil418
Password: 44=*LfB4NgQ,

