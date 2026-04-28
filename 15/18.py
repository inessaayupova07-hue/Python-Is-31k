from datetime import datetime

deadline = datetime.strptime(input("Дедлайн (YYYY-MM-DD): "), "%Y-%m-%d")

if datetime.now() > deadline:
    print("Дедлайн просрочен")
else:
    print("Дедлайн ещё не наступил")
