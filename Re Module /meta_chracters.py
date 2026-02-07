import re


# test_string = "123abc456789abc123ABC"
test_string = "hello 123_ heyho hohey"

# pattern = re.compile(r".")
# pattern = re.compile(r"\.")
# pattern = re.compile(r"^abc")
# pattern = re.compile(r"\d")
# pattern = re.compile(r'\D')
# pattern = re.compile(r"\s")
# pattern = re.compile(r"\S")
# pattern = re.compile(r"\w")
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\bhey')
pattern = re.compile(r'\Bhey')

matches = pattern.finditer(test_string)

for match in matches:
    print(match)