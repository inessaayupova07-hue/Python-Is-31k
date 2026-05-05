class SafeFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
            return self.file
        except Exception as e:
            print("Error:", e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("File closed")
        if hasattr(self, "file"):
            self.file.close()

with SafeFile("input.txt") as f:
    if f:
        print(f.read())
