import re
log = "2026-04-01 INFO Start"
match = re.match(r"(\d{4}-\d{2}-\d{2})\s+(INFO|ERROR)\s+(.*)", log)
if match:
    print(match.groups())