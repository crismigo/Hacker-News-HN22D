class Counter:
    count = 0

    def __getattr__(self, item):
        return self.count

    def increment(self):
        self.count += 1
        return ""
    def decrement(self):
        self.count -= 1
        return ""
    def double(self):
        self.count *= 2
        return ""