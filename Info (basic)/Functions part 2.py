
# Example of a function
def greet():
    print("Hello Angela")
    print("How do you do Jack Bauer?")
    print("Isn't the weather nice today?")


greet()


# Functions can have an input.
# 'name' is the parameter.
# 'Jack Bauer' is the argument.
# def function_name(parameter)
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


# function_name(argument)
greet_with_name("Jack Bauer")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Calling greet_with() with Positional Arguments (inputs)
# Positional since which name goes where just depends on the order you write them into the argument
# Can have more than two
greet_with("Jack Bauer", "Nowhere")
# vs.
greet_with("Nowhere", "Jack Bauer")


# Calling greet_with() with Keyword Arguments (inputs)
# These arguments can be switched around, it doesn't matter which order you write them in
greet_with(location="London", name="Angela")


# example:
import math
def paint_calc(height, width, cover):
    number_of_cans = ((height*width)/cover)
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint.")
# Define a function called paint_calc() so that the code below works.
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
