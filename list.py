# lists , a list holds objects
my_list = [1, 5, 8, 9, 51, 4]
ma_liste = [1, "Hello", 4.3, True, [1, 2, 3]]

# print(my_list)
# print(ma_liste)

names = ["tim", "joe", "john", "james"]

# add one more person to our names list at the end
names.append("alex")
# print(names)

# add one more person to our names list at the beginning
names.insert(0, "olivier")
# print(names)

# add one more person to our names list at the indexed chosen position
names.insert(3, "Toto")
# print(names)

# remove one person from our list
names.remove("alex")
# print(names)

# reversing our list
names.reverse()
# print(names)

# sorting our numbers
my_list.sort()
# print(my_list)

# iterate on our list with a for. a list is iterable. iterable means we can iterate over it
# for i in my_list:
# print(i)

##### Advanced lists #####
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number_list)

# negative indexing [-1] to print the last element of the list, -2 for the one before etc etc
# print(number_list[-2])

# put a range element
3 firsts index
# print(number_list[:3])

# from first element to last element, excluding the last one
# print(number_list[:-1])

# from element 5 until the end
# print(number_list[5:])

# jump 2 by 2
# print(number_list[0:10:2])

# jump 3 by 3
# print(number_list[0:10:3])

# full list
# print(number_list[::])

# full list reversed
# print(number_list[::-1])

# for loop, with i variable, which go to 0 to 9. everytime there is a loop, we print from the beginning until n+1
for i in range(len(number_list)):
# print(number_list[:i])

# in our list we want to get group of 3, 0 1 2,1 2 3, 2 3 4, 4 5 6, etc. if we don't put our window_size-1, we end up with few useless lines at the end
window_size = 3
for i in range(len(number_list)-(window_size-1)):
#     print(number_list[i:i+window_size])
