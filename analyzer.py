class VolatilityAnalyzer:
    def __init__(self):
        self.history = []
    def add_tick(self, digit):
        self.history.append(digit)
        if len(self.history) > 100:
            self.history.pop(0)
    def predict(self):
        if len(self.history) < 10:
            return None
        avg = sum(self.history[-10:]) / 10
        if avg < 4.5:
            return "OVER 3"
        else:
            return "UNDER 6"
