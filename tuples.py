# a tuples is a list with parenthesis. The difference with a list is, you can't change what's inside tuples (can't add or remove elements)
t = (1, 2, 3)
# the point to use a tuple is to be more secure for exemple :
credit_card1 = (1234123412341234, "Joe Tatin", "11/25", 354)
credit_card2 = (1234123412341234, "Joe Tatin", "11/25", 354)

# put our tuples in a list, so our credit card numbers can't be changed
credit_cards = [credit_card1, credit_card2]
print(credit_cards)

# unpacking a tuple, to use separately
person1 = ("Nancy", 25, "Pizza")
person2 = ("Tom", 31, "Pasta")

# creating a list of 2peoples where each person is a tuple
people = [person1, person2]

# (name, age, favFood) = person

# print(name)
# print(age)
# print(favFood)

for name, age, favFood in people:
    print(name)
    print(age)
    print(favFood)
    print()
