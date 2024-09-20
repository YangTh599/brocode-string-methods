# Thayer Yang
# 20 SEP 2024
# BroCode

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. uesrname must not contain digits

username = input("Enter a username: \n")

if len(username) > 12:
    print("Username can't be more than 12 characters")
elif not username.find(' ') == -1:
    print("Username can't contain spaces")
elif not username.isalpha():
    print("Username can't contain numbers")
else:
    print(f'Hello {username}.')