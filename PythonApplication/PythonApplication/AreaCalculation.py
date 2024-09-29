# Import the math module to use the value of pi
import math

# Function to calculate area of a circle
def calculate_area(radius):
    # Formula: Area = pi * radius^2
    area = math.pi * radius**2
    return area

# Input: radius from user
radius = float(input("Enter the radius of the circle: "))

# Calling the function and displaying the result
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")





