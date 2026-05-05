from multiprocessing import Pool

def heavy(n):
    return sum(i*i for i in range(n))

with Pool(4) as p:
    print(p.map(heavy, [1000000]*4))
