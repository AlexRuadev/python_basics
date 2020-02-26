# import regular expression
import re

text = "random string. MyName123@website.com . some more random text and email . toto678@company.net"

# create a regular expression pattern
pattern = re.compile("[rdm]")

# find anything with lower case, uppercase, or with 0-9
pattern1 = re.compile("[a-zA-Z0-9]+")

# find email adress in a text
pattern2 = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.+[a-zA-Z0-9-.]+")

# meaning : i want to search my text using the pattern. the search function stop after the first match. findall() function finds everything
result = pattern2.search(text)
result2 = pattern2.findall(text)
print(result)
print(result2)
