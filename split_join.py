# Split, take a string to put in a list
problems = "broke, page, short, nerdy"
print(problems)

# take our problems string to put it in a liste, and our delimitator is a ", "
my_list = problems.split(", ")
print(my_list)

# Join, join a list together into a string
joined = " and ".join(my_list)
print(joined)

# to write a csv file, put your join in a variable
csv = ",".join(my_list)
print(csv)
