import re
print('=== Account Registration ===')
username = input('enter your username: ')
pattern = input('enter your password: ')
pattern = r"^{5,}$"
while True:
    print("Password valid!! Account created.")
    break
else:
    print("\npassword not valid!!! please follow the rules")
    print("- at least 5 characters\n")
    print("try again.\n")