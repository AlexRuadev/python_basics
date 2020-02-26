# if lists aren't the same size, python truncate the longer list so it equals the shorter one
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['one', 'two', 'three', 'four', 'five']
zipped = list(zip(list1, list2))
# print(zipped)


list1 = [1, 2, 3, 4, 5]
list2 = ['one', 'two', 'three', 'four', 'five']

# To use zip it's not required to have same sized list, but it's cleaner
# it takes the correspondig element of each list and put them together
zipped = list(zip(list1, list2))
# print(zipped)

# unzip our zipped lists, using the *. they are put in a list of 2 tuples
unzipped = list(zip(*zipped))
# print(unzipped)

# itereate over our both list with a for loop
# for (l1, l2) in zip(list1, list2):
# print(l1)
# print(l2)

# exemples :
items = ['Apple', 'Banana', 'Orange']
counts = [3, 6, 4]
prices = [0.99, 0.25, 0.50]

sentences = []
for (item, count, price) in zip(items, counts, prices):
    # put them all in a string
    item, count, price = str(item), str(count), str(price)
    sentence = 'I bought ' + count + ' ' + item + 's at ' + price + ' cts each.'
    sentences.append(sentence)
print(sentences)
