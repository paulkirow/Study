from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        value = self.cache_dict.pop(key)
        self.cache_dict[key] = value
        return self.cache_dict[key]

    def put(self, key: int, value: int) -> None:
        while len(self.cache_dict) >= self.capacity:
            self.cache_dict.pop(list(self.cache_dict.keys())[0])
        self.cache_dict[key] = value

    def __str__(self):
        return str(self.cache_dict)
# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)

print(str(obj.put(1,7))+"	"+str(obj))
print(str(obj.put(2,6))+"	"+str(obj))
print(str(obj.get(1))+"	"+str(obj))
print(str(obj.put(3,3))+"	"+str(obj))
print(str(obj.get(2))+"	"+str(obj))
print(str(obj.put(4,4))+"	"+str(obj))
print(str(obj.get(1))+"	"+str(obj))
print(str(obj.get(3))+"	"+str(obj))
print(str(obj.get(4))+"	"+str(obj))