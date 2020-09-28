class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.items = []

    def append(self, item):
        if len(self.items) is self.capacity:
            self.items[self.index] = item
        else:
            self.items.append(item)

        self.index = (self.index + 1) % self.capacity
            

    def get(self):
        return self.items