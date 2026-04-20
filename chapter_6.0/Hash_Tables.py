class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'

class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0
    
    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        return len(key) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.
        
        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        
        # Start to search from the given position
        current = start
        
        # while self.slots "start position" is not empty: اذا المكان مشغول مو فارغ
        while self.slots[current] is not None:
        # (index + 1) % size = next index position
            current = (current + 1) % self.size
            
            # if we went throgh all list index and we are back to the started one return empty list to not be infint loop إذا رجعنا لنفس البداية
            if current == start:
                return None

        return current
    

    def _find_key(self, start, key):
        """
        Starting from 'start' try to find 'key'.

        Parameters:
        - 'start': Starting index
        - 'key': The key to be found

        Returns: The index position of the key or None if not found
        """
        # Start to search from the given position
        current = start

        # While current position is occupaid and it's not the key, enter the loop
        while self.slots[current] and self.slots[current].key != key:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size
            # If we reach again the given position, that means
            # a whole cycle has been completed and the key was not found
            if current == start:
                return None

        # After the loop, current points to a free position or
        # to the position with the key
        if self.slots[current]:
            return current
        else:
            return None

    def put(self, key, value):
        """
        Add or updates a key with a value in the hash table

        Parameters:
        - 'key': The key to add or update.
        - 'value': The value of the key

        Returns: None
        """
        # Raise an error if no space available
        if self.used_slots == self.size:
            raise(MemoryError('Hash table is full'))
        #  Try to find the key
        h = self._hash(key)
        q = self._find_key(h, key)
        if q is not None:
            # If found, update the value
            self.slots[q].value = value
        else:
            # If not found, find a free slot
            q = self._find_free_slot(h)
            # Add a new element.
            self.slots[q] = HashItem(key, value)
            # And increase used_slots
            self.used_slots += 1


    def get(self, key, alternative=None):
        """
        Get the value of 'key'.
        Parameters:- 'key': The key to find- 'alternative': An alternative value if key is not found. 
        Optional. Default value=None
        Returns: The value of 'key' or alternative value
        """
        # Try to find the key        
        h = self._hash(key)
        q = self._find_key(h, key)
        if q is None:
            # If key was not found return None
            return alternative
        else:
            # If key was found, return the value of the key
            return self.slots[q].value
        
            