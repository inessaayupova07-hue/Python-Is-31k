from multiprocessing import Process

def calc():
    print(sum(range(1, 100001)))

p1 = Process(target=calc)
p2 = Process(target=calc)

p1.start()
p2.start()

p1.join()
p2.join()
