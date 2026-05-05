import threading
import time

def daemon_task():
    while True:
        print("Running...")
        time.sleep(1)

t = threading.Thread(target=daemon_task, daemon=True)
t.start()

time.sleep(3)
print("Main finished")
