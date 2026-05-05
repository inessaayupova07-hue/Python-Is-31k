import time
import threading
from multiprocessing import Process

def calc():
    sum(range(1, 1000000))

# threading
t1 = threading.Thread(target=calc)
t2 = threading.Thread(target=calc)

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
print("Threading:", time.time() - start)

# multiprocessing
p1 = Process(target=calc)
p2 = Process(target=calc)

start = time.time()
p1.start()
p2.start()
p1.join()
p2.join()
print("Multiprocessing:", time.time() - start)
