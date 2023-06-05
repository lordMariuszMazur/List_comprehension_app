# List comprehension.

# Passible forms l.c.:
# expr - expression, val- value, collection=list
# [ expr for val in collection]
# [expr for val in collection if <test1> and <test2>]
# [expr for val1 in collection1 and val2 in collection2]

# 1. List of squares with loop 100 positive integers.
squares = []
for i in range(1, 101):
    squares.append(i**2)

print("Standard list: ", squares)  # result

# Easiest way. List comprehension, in one line. Same result.

squares2 = [i**2 for i in range(1, 101)]
print("List comprehension: ", squares2)  # result

# 2. Create a list of remainders contains first 100 squers
# divide by 5. Symbols: %: divide, **2: squere
remainders5 = [x**2 % 5 for x in range(1, 101)]
print("List remainder by 5: ", remainders5)  # result

remainders11 = [x**2 % 11 for x in range(1, 101)]  # remainders by 11
print("List remainder by 11: ", remainders11)

# 2. Find movies start from a letter G. Using if.
movies = [
    "Star Wars",
    "Gattaca",
    "Ghostbusters",
    "Toy Story",
    "Troy",
    "Groundhog Day",
    "Batman",
    "Citizen Kane",
]

# Without l.c.
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print("Without l.c.: ", gmovies)

# Using l.c.
gmovies2 = [title for title in movies if title.startswith("G")]
print("With l.c.: ", gmovies2)

# 3. Find movies released before 2000.
movies2 = [
    ("Star Wars", 1977),
    ("Gattaca", 1997),
    ("Ghostbusters", 1984),
    ("Toy Story", 1995),
    ("Troy", 2004),
    ("Groundhog Day", 1993),
    ("Batman", 1989),
    ("Citizen Kane", 1941),
]

pre2k = [title for (title, year) in movies2 if year < 2000]
print("List before 2k: ", pre2k)  # result

# 4. Scalar multiplication.
v = [2, -3, 1]

w = [4 * x for x in v]  # l.c. solution
print("Scalar m.: ", w)  # result

# 5. Cartesian product.
""" If A and B are sets, then the Cartesian product
is the set of pairs (a,b)
where a is in A and b is in B."""

A = [1, 3, 5, 7]  # list of odd integers
B = [2, 4, 6, 8]  # list of even integers

cartesian_product = [(a, b) for a in A for b in B]  # formula
print("Cartesian product: ", cartesian_product)  # result
