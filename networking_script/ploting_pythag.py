import numpy 
import matplotlib.pyplot as plt

#destinations = [[10,40], [40,60],[80,60],[-20,30],[-50,-20]]

x = [10, -18, 25,9,17,3,-15,0,-20]
y = [40, 27, 43,24,35,26,13,35,0]

plt.scatter(x, y, marker='o', linestyle='-')
# Function to calculate the hypotenuse of a right triangle
plt.grid(True)  # Add grid for better visibility
plt.show()


"""
def calculate_hypotenuse(a, b):
    return numpy.sqrt(a**2 + b**2)
"""