import random, os
from datetime import datetime

nums=[random.randint(1,100) for _ in range(5)]

with open('numbers.txt','w') as f:
    f.write(str(nums)+'\n')
    f.write(str(datetime.now()))

print(os.path.exists('numbers.txt'))

with open('numbers.txt','r') as f:
    print(f.read())