# Functions: If, Then and Else.

# 1. If. Collect string / test length.
raw_input=input('Please enter a test string: ')
if len(raw_input)<6:
    print('Your string is too short.')
    print('Please enter a string with at least 6 characters.')

# 2. If and Else. Prompt user to enter number / test if even or odd.
user_input=input('Please enter an integer: ')
number=int(user_input)

if number % 2 == 0:
    print('Your number is even.')
else:
    print('Your number is odd.') 

# 3. If, Else, Elif. Triangle trest.
# Scalene triangle: All sides have different lengths.
# Isosceles triangle: Two sides have the same length.
# Equilateral triangle: All sides are equal.
a=int(input('The length of side a = '))
b=int(input('The length of side b = '))
c=int(input('The length of side c = '))

if a != b and b != c and a != c:
    print('This is a scalene triangle.')
elif a==b and b==c: # elif = else if
    print('This is an equilateral triangle.')
else:
    print('This is isosceles triangle.')