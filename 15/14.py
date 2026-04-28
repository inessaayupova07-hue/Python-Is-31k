from datetime import datetime

birth = datetime.strptime(input("Дата рождения (YYYY-MM-DD): "), "%Y-%m-%d")
today = datetime.now()

print((today - birth).days)
