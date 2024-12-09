class HashTables:
    def __init__(self):
        self.MAX = 10
        self.array = [[] for _ in range(self.MAX)]  # Initialize buckets

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.array[h].append((key, val))  # Always append the key-value pair

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.array[h]:
          if element[0] == key:
            return element[1]


    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, kv in enumerate(self.array[h]):
           if kv[0] == key:  # Check if the key matches
             del self.array[h][index]
        
# Example Usage
t = HashTables()
t['march 6'] = 120
t['march 17'] = 397  # Appends a new entry with the same key
#print(t['march 6'])  # Should print: [('march 6', 120), ('march 6', 397)]
#print(t.array)
print(t.array)
del (t['march 6'])
print(t.array)