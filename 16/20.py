import re
text = """2026-04-01 ERROR Failed
2026-04-01 INFO OK
2026-04-02 ERROR Crash"""
errors = re.findall(r"(\d{4}-\d{2}-\d{2})\s+ERROR", text)
from collections import Counter
print(Counter(errors))