class student:
    def __init__(self, name, address, phonenumber):
        self.name = name
        self.address = address
        self.phoneNumber = phonenumber
    def welcome(self):
        print(f"welcome, {self.name}!")
        print(f"welcome, {self.address}!")
        print(f"welcome, {self.phoneNumber}!")
        print("we are happy to have you in our school")
        print("=== student registration system ===")
name_input = input(" enter your name:")
address_input = input("enter your address:")
phoneNumber = input("enter your phone number:")
new_student = student(name_input, address_input, phoneNumber)
new_student.welcome() 