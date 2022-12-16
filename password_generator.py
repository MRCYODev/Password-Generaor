import random

# List of possible characters for the password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\"<>,.?/"

# Ask the user how long they want their password to be
length = int(input("Enter the length of the password: "))

# Generate a random password using the possible characters and the specified length
password = "".join(random.sample(chars, length))

# Print the generated password
print("Your password is:", password)