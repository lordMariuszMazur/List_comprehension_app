# Sets
# Do not store the duplicates, it is mutable,
# The order of elements in set() does not matter.

example = set()
# dir(example) # explains the functions in set()
# help(example.add) # more info about add in set()

# 1. Method 'add'

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print("Add: ", example)  # print the content of set()
print(len(example))  # length of set()

# Enumarate

entry = enumerate(example, 1)
output_entry = type(entry)
list_entry = list(entry)


def enu():
    for index, element in list_entry:
        print("Index: ", index, "related element: ", element)


# enu() # calls the function

# 2. Method 'remove'
"Remove an element from a set, if is not a member, raise a KeyError"

example.remove(42)
print("Remove:(42) ", example)  # print the content of set()

# 3. Method 'discard'
"Remove an element from a set, if is not a member, do nothing"

# help(example.discard) # help for discard

# Other way, faster.

example2 = set([28, "True", 2.71828, "Helium"])  # adds faster than using 'add' method
example2.clear()  # removes all elements from a set

# Union
"Contains all elements in set A and set B"

# Intersection
"Set of elements inside both A and B"

# Example. Integers 1-10

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print(odds.union(evens))
"{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"  # result
evens.union(odds)
"{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"  # same result
odds.intersection(primes)
"{3, 5, 7}"  # result
primes.intersection(evens)
"{2}"
composites.difference(evens)
"{9}"
evens.intersection(odds)
"set()"  # result means an empty set

# Operator 'in'
"Tests if an element is inside a set"

2 in primes  # question: Is number 2 in set 'primes' ?
"True"  # result means 'yes'
3 in composites
"False"  # result means 'no'

# Operator 'not in'
" Tests if an element is NOT inside a set"

9 not in evens  # question: Is not number 9 in set 'evens' ?
"True"  # result means 'no', evens do not have number 9

# Method 'issubset'
" Report whether another set contains this set"

evens.issubset(primes)
"False"  # result means 'no', not all set evens is in set primes
