# a set is another way to group things. you can't have duplicates in a set, and it's in a random order.

# my_set = {"banana", "blueberry"}
# print(my_set)


# add more items to our set
# my_set.add("mango")
# print(my_set)

# add a duplicate to try. it didn't get added cause duplicate aren't allowed in a set
# my_set.add("mango")
# print(my_set)

######################

list_of_fruits = ["banana", "raspberry", "cherry",
                  "cherry", "apple", "mango", "banana"]

# cast our list in a set to remove automatically duplicates
remove_duplicate = set(list_of_fruits)
# print(remove_duplicate)

# cast our set back into a list without duplicates
no_duplicate_list = list(remove_duplicate)
# print(no_duplicate_list)

# assigning notre no_duplicate_list to list_of_fruits to re write it
list_of_fruits = no_duplicate_list
# print(list_of_fruits)

#######################
library_1 = {"Harry Potter", "Hunger Games", "Lord of the Rings"}
library_2 = {"Harry Potter", "Romeo and Juliet"}

# putting our 2 library together and automatically remove our duplicate
our_books = library_1.union(library_2)
print(our_books)

# putting our 2 library together and printing commons books with intersection
common_books = our_books = library_1.intersection(library_2)
print(common_books)

# calling the library1 to see the difference with library2.
diff_books = library_1.difference(library_2)
print(diff_books)

# calling the library2 to see the difference with library1.
diff_books = library_2.difference(library_1)
print(diff_books)

# to clear our set
diff_books.clear()
print(diff_books)
