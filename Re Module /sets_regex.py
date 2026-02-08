import re

test_string = "helloHELLO 123-_"

# pattern = re.compile(r'[lo]')
# pattern = re.compile(r'[a-z]')
# pattern = re.compile(r"[0-9-]")
pattern = re.compile(r"[a-zA-Z0-9]")
matches = pattern.finditer(test_string)

for match in matches :
    print(match)