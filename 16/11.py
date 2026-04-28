import re
text = "I am at home"
print(re.sub(r"\b\w{1,2}\b", "***", text))