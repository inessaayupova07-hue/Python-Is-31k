import re
text = "pass1234"
print(bool(re.fullmatch(r"(?=.*\d).{8,}", text)))