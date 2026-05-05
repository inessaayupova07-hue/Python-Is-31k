class Timer:
    __slots__ = ('start', 'end')

    def diff(self):
        return self.end - self.start

t = Timer()
t.start = 10
t.end = 25
print(t.diff())
