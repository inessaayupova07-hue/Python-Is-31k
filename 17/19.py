import random
from datetime import datetime, timedelta

start=datetime(2024,1,1)
end=datetime(2024,12,31)
delta=(end-start).days
random_day=start+timedelta(days=random.randint(0,delta))
print(random_day)