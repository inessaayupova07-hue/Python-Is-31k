with open("log.txt", "r") as f:
    print(sum(1 for line in f if "ERROR" in line))
