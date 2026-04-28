import re
text = "1234 5678 9012 3456"
print(re.sub(r"\d(?=\d{4})", "*", text))