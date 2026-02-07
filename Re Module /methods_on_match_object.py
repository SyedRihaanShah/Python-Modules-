import re
#group , start, end, span

test_string = "123abc456781abc123ABC"

pattern = re.compile(r"abc")
matches = list(pattern.finditer(test_string))
print(matches)

for match in matches:
    # print(match.span(), match.start(), match.end())
    print(match.group())
