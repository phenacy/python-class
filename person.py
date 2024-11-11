# Define the Person class
class Person:
    def __init__(self, name, age, gender):
        self.name = name  # Initialize the 'name' attribute
        self.age = age    # Initialize the 'age' attribute
        self.gender = gender  # Initialize the 'gender' attribute

    def introduce(self):
        # Print a message introducing the person
        print(f"Hello, my name is {self.name}. I am {self.age} years old and my gender is {self.gender}.")

# Create an instance of the Person class
person1 = Person("Phenacy", 22, "Male")

# Call the introduce method to display the person's information
person1.introduce()
