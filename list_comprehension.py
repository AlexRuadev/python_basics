names = ["Jennifer", "Susan", "Jane", "Sophie"]

# we create a new list
my_liste = []

#############################################
# the two next blocs are exactly the same, one with a for loop, one with a comprehension list

# we loop over that list and put everything in it
for person in names:
    my_liste.append(person)
print(my_liste)

# comprehension list
print([person for person in names])

#############################################

ma_liste = []

#############################################
# the two next blocs are exactly the same, one with a for loop, one with a comprehension list

# we loop over that list and put everything in it
for person in names:
    ma_liste.append(person + " dumped me. ")
print(ma_liste)


# comprehension list
print([person + " dumped me." for person in names])

#############################################

movies_and_ratings_dict = {"Interstellar": 9,
                           "Dark Knight": 8, "Harry Potter": 6, "50 Shades": 2}

movies_and_ratings_list = []
# want to show only movies with ratings above 6
for movie in movies_and_ratings_dict:
    if movies_and_ratings_dict[movie] > 6:
        movies_and_ratings_list.append(movie)
print(movies_and_ratings_list)

# same code with line comprehension.
print([movie for movie in movies_and_ratings_dict if movies_and_ratings_dict[movie] > 6])
