# Classes. Class Features.
class User:
    pass


user1 = User()  # creates user1 in class User
user1.first_name = "Dave"
user1.last_name = "Lombardo"

# print(user1.first_name, user1.last_name)

user2 = User()  # creates user2 in class User
user2.first_name = "Frank"
user2.last_name = "Castle"

# print(user2.first_name, user2.last_name)

first_name = "Arthur"  # simple string
last_name = "Pascano"

# print(first_name,last_name)

# Class features ( methods, initialization, help text)
# init = initialization or 'Constructor'
import datetime


class Mate:
    """A member of Metallica. For now we are
    only storing their name and birthday.
    But soon we will store an uncomfortable
    amount of mate informatipon."""  # also called Docstring

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyymmdd

        # Extract first and last names.
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Returns the age of the mate in years"""  # needs datatime
        today = datetime.date(2021, 10, 2)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)  # Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


mate = Mate("Lars Ulrich", "19710315")

# print(mate.name,mate.birthday)
# print(mate.first_name)
# print(mate.last_name)

# help(Mate) # prints the help option for Mate class

print(mate.name, "is: ", mate.age(), "years old.")
