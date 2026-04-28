from datetime import datetime

now = datetime.now()
timestamp = now.timestamp()

print("UNIX timestamp:", timestamp)
print("Обратно:", datetime.fromtimestamp(timestamp))
