# Marquies White
# Module 12 Lab
# CIS129
# 12/1/2024

# The main function
def main():
    print()

    # Declare input variables
    # These inputs will prompt the user with various questions
    input_name = input("Enter the pet's name: ")
    input_type = input("Enter the pet's type: ")
    input_age = int(input("Enter the pet's age: "))

    # Class variable to hold a pet
    # Creates the Pet class and sets the field to private
    # The constructor
    class Pet:
        def __init__(self, name, type, age):
            self._name = name
            self._type = type
            self._age = age
    # Creates an instance of the Pet class with the Animal variable
    Animal = Pet(input_name, input_type, input_age)



    # Displays the pet's inputted information
    print(f"The pet's name is {Animal._name}")
    print(f"The pet's type is {Animal._type}")
    print(f"The pet's name is {Animal._age}")

    # The mutators
    def set_name(self, name):
        self._name = name
    
    def set_type(self, type):
        self._type = type
    
    def set_age(self, age):
        self._age = age

    # The accessors
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.type
    
    def get_age(self):
        return self.age
    
# Calls the function
main()