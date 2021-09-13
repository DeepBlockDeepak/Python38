class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size #map is a list of 'size' elements 

    #_get_hash assigns a hashed value based on the ASCII value of the 'key' argument
    def _get_hash(self,key):
        hash = 0 #initialize hash
        
        #loop through the 'key' arguement. Modulo by 'size' to obtain index values between 0-5.
        for char in key:
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = [key_value]
            return True
        
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)#collision handling
            return True

    def get(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is not None:            
            for pair in self.map[key_hash]:                
                if pair[0] == key:
                    return pair[1]

        return None


    def delete(self,key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        
        for i in range(len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def print(self):
        print ("-"*5, "Phonebook", "-"*5)
        for item in self.map:
            if item is not None:
                print (str(item))

h= HashMap()
h.add("Bob", '303-8888')
#h.add("Jessie", "505")
h.add("Bill", "404")
h.add("Bill", "666")
h.print()
print ("===============")

print (h.map)
print (h.get("Bill"))

