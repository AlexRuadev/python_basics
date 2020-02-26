my_groceries_dictionnary = {"bananas": 10, "oranges": 3, "apples": 15}

# get elements from dictionnay. we need to have the key to get the values. .get() doesn't return an error if the key isn't in dictionnary
# print(my_groceries_dictionnary.get("bananas"))


contacts_dict = {
    "Joe": {"phone": "+23-4567-8597", "email": "joe@hotmail.com"},
    "Jane": {"phone": "+23-4595-7896",  "email": "jeanne@gmail.com"}
}
# get Joe phone informations
# print(contacts_dict["Joe"])

# get Joe email
# print(contacts_dict["Joe"]["email"])


# count the words and count how many time it appears in a sentence with a dictionnary
sentence = "I like the name Alex because the name Alex is the best"

word_counts = {
    "I": 1,
    "like": 2,
    "the": 3
}

# add to a dictionnary manually
word_counts["Aaron"] = 2
print(word_counts)

# sorting a dictionnary. with .items() we get a dictionnary object. add it into list() to get a list
# print(word_counts.items())

# getting only keys
# print(word_counts.keys())

# getting only values
# print(word_counts.values())

# delete something from dictionnary. pop() remove an element by calling it keys. 
# word_counts.pop("like")
# print(word_counts)

# deleting an arbitrary item, which is the last one, and give us back a tuple
# word_counts.popitem()
# print(word_counts)

# deleting our dictionnary, to make it empty
# word_counts.clear()
# print(word_counts)

# getting a list of our values, and sort it 
print(sorted(list(word_counts.values())))