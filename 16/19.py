import re
text = "Name: John Age: 25"
match = re.search(r"Name:\s(\w+)\sAge:\s(\d+)", text)
if match:
    print(match.groups())