import re

#methods -> match(), search(), findall()

test_string = "123abc21-0430abc7493abc"

pattern = re.compile(r"abc")

# matches = pattern.finditer(test_string) #returns the whole object
# matches = pattern.findall(test_string)#just prints the strings
# match = pattern.match(test_string)#only looks for the pattern at the begnegging 
match = pattern.search(test_string)#returns the first span of the pattern 


print(match)
# for match in matches:
#     print(match)