import threading
import time

def worker():
    for i in range(5):
        print(i)
        time.sleep(1)

t = threading.Thread(target=worker)
t.start()
t.join()
