class CircularBuffer:
    def __init__(self, length):
        self.length = length
        self.values = []
    
    def add(self, value):
        self.values.append(value)
        if len(self.values) > self.length:
            self.values.pop(0)
    
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, index):
        return self.values[index]