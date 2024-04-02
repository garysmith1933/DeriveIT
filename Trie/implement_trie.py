class Strings:
    
    def __init__(self):
        self.root = {}
        
        
    def add(self, string): # O(m) - length of the string we have to add
        node = self.root

        for char in string:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['endOfWord'] = True
    
    def hasPrefix(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node:
                return False
            
            node = node[char]
        
        return True
        
    def has(self, string): # O(1)
        node = self.root # current node

        for char in string:
            if char not in node:
                return False
            
            node = node[char]
        
        return 'endOfWord' in node
        