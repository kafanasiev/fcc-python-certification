class HashTable:
    def __init__(self):
        self.collection = {}
    def hash(self,string = str):
        hashed_value = 0
        for ch in string:
            hashed_value += ord(ch)
        return hashed_value
    def add(self,key, value):
        new_key = self.hash(key)
        if new_key not in self.collection:
            self.collection[new_key] = {}
        self. collection[new_key][key] = value

    def remove(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            del self.collection[hash_key][key]
            if not self.collection[hash_key]:
                del self.collection[hash_key]
       


    def lookup(self, key):
        hash_key = self.hash(key)
        if hash_key in self.collection and key in self.collection[hash_key]:
            return self.collection[hash_key][key]
        else:
            return


hash_table = HashTable()
hash_table.add('golf', 'sport')
hash_table.add('flog', 'backwards golf')
print(hash_table.collection)