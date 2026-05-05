import threading
import queue

def worker(q):
    while not q.empty():
        print(q.get())
        q.task_done()

q = queue.Queue()
for i in range(5):
    q.put(i)

threads = []
for _ in range(2):
    t = threading.Thread(target=worker, args=(q,))
    threads.append(t)
    t.start()

q.join()
