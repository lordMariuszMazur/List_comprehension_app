# Map, Filter and Reduce functions.

# False values(empty): '',0,0.0,[],(),{},False,None and
# instances which signal they are empty.
# Sometimes '0' is an important pieces of data.

# Map: map(function,data).
# 1. Compute radius for different circles.

import math


def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)


radii = [2, 5, 7.1, 0.3, 10]  # list of r in different circles

# Method 1: Direct method.

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print("Result 1: ", areas)

# Method 2: Use 'map' function.
map(area, radii)  # the output is a map object not a list, so:
print("Result 2:", list(map(area, radii)))  # result is a list

# 2. Compute the temperature from C to F.
# Formula: F=(9/5)*C+32
temps = [("Berlin", 29), ("Cairo", 36), ("Tokyo", 27), ("Buenos Aires", 19)]

c_to_f = lambda data: (data[0], (9 / 5) * data[1] + 32)
print("Result C to F: ", list(map(c_to_f, temps)))

# Filter. Function is used to select certain pieces of data
# from a list,tuple etc.

# 1. Find all data above the average.

import statistics

data1 = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data1)  # compute average(mean)
print("AVG is:", avg)  # check avg

solution = filter(lambda x: x > avg, data1)
print("Above AVG: ", list(solution))  # result

# or data below avg
print("Below AVG:", list(filter(lambda x: x < avg, data1)))

# 2. Remove missing data.
countries = ["", "Argentina", "", "Brasil", "Chile", "", "", "Ecuador", "Venezuela"]
data2 = list(filter(None, countries))  # None insted of ''
print("List of countries in South America:", data2)  # result

# Reduce.
"""Use functools.reduce() if you need it;
however,99% of the time an explicit
for loop is more readable. GvR"""

from functools import reduce

# 1. Multiple all numbers in a list.
data3 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Method 1. Easier way.
multiplier = lambda x, y: x * y
print("Result with reduce: ", reduce(multiplier, data3))

# Method 2. More readable way.
product = 1
for x in data3:
    product = product * x

print("Result without reduce: ", product)
