from datetime import datetime

message = input("Введите сообщение: ")

with open("messages.log", "a", encoding="utf-8") as f:
    f.write(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {message}\n")
