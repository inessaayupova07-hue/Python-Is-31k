import threading
import time

def download(name):
    print(f"Start {name}")
    time.sleep(2)
    print(f"End {name}")

threads = []
for i in range(3):
    t = threading.Thread(target=download, args=(f"File-{i}",))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
