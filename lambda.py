# Lambda expressions. Simple function usualy for one use.

# 1. Write a function to compute 3x+1

# standard function:
def f(x):
    return 3 * x + 1


print(f(2))  # should be f(2)

# or lambda option:
g = lambda x: 3 * x + 1
print(g(3))  # should be g(3)

# 2. Combine first and last name into a single 'Full Name'

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("  antonio", "BANDERAS"))  # should be full_name(' antonio', 'BANDERAS')

# 3. Sort list in alphabetical order.
scifi_authors = ["Isaac Asimov", "Julius Verne", "Stanislaw Lem", "H. G. Wells"]

help(scifi_authors.sort)  # help and explanation request

# expected :
"""Help on built-in function sort:

sort(*, key=None, reverse=False) method of builtins.list instance
    Sort the list in ascending order and return None.
    
    The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
    order of two equal elements is maintained).
    
    If a key function is given, apply it once to each list item and sort them,
    ascending or descending, according to their function values.
    
    The reverse flag can be set to sort in descending order."""

# finall code:
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)  # should be scifi_authors
# if not work well try:
sorted(scifi_authors)


# 4. Quadratic functions
# f(x) = ax^2 + bx + c


def q_f(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a * x**2 + b * x + c


f = q_f(2, 3, -5)
print(f(0))  # should be f(0)

# or different possibility:
q_f(3, 0, 1)(2)  # f(x) = ax^2 + bx + c evaluated for x=2
print(q_f(3, 0, 1)(2))  # f print is used only in VSC
