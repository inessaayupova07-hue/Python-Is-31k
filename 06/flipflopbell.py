class FlipFlopBell:
    def __init__(self):
        self.state = True

    def ring(self):
        if self.state:
            print("flip")
        else:
            print("flop")
        self.state = not self.state
