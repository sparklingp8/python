BLANK = object()


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.values = capacity * [BLANK]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        index = hash(key) % len(self)
        self.values[index] = value

    def __getitem__(self, key):
        index = hash(key) % len(self)
        value = self.values[index]
        if value is BLANK:
            raise KeyError(key)
        return value

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default


sample_data = HashTable(capacity=100)
sample_data["hola"] = "hello"
sample_data[98.6] = 37
sample_data[False] = True
x = "hola" in sample_data
print(x)
