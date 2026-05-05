import threading
import queue

def worker(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Processing {item}")
        q.task_done()

q = queue.Queue()
threads = []
for _ in range(3):
    t = threading.Thread(target=worker, args=(q,))
    t.start()
    threads.append(t)

for i in range(5):
    q.put(i)

q.join()

for _ in threads:
    q.put(None)

for t in threads:
    t.join()
