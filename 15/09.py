files = ["file1.txt", "file2.txt"]

with open("result.txt", "w", encoding="utf-8") as outfile:
    for filename in files:
        with open(filename, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())
            outfile.write("\n")
