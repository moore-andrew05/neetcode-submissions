class MyHashSet:
    def __init__(self):
        self.size = 512
        self.buckets = [[]] * self.size

    def _hash(self, key):
        return key % self.size
        
    def add(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if len(bucket) == 0:
            bucket.append(key)
            return

        for val in bucket:
            if val == key:
                return

        bucket.append(key)
            
    def remove(self, key: int) -> None:
        bucket = self.buckets[self._hash(key)]
        if len(bucket) == 0:
            return
        
        for i, val in enumerate(bucket):
            if val == key:
                bucket.pop(i)
                return
        
    def contains(self, key: int) -> bool:
        bucket = self.buckets[self._hash(key)]
        if len(bucket) == 0:
            return False
        
        if len(bucket) == 1 and bucket[0] == key:
            return True

        if len(bucket) > 1:
            for val in bucket:
                if val == key:
                    return True

            return False

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)