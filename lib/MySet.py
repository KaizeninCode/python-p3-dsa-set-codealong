class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary # the in keyword will return true or false
    
    def add(self, value):
        self.dictionary[value] = True # Add a value as a key into the dictionary
        return self                   # Return the updated set
    
    def delete(self, value):
        self.dictionary.pop(value, None) # None is an optional argument and is the return   value if the value does not exist in the dictionary

    def size(self): # returns the number of elements in the set
        return len(self.dictionary)    
    
    def clear(self): # removes all the items from the set and returns the updated set
        self.dictionary.clear() # removes all the items from the set
        return self.dictionary # returns the updated set
    
    # return a string that only contains the values of the dictionary, separated by commas. You can achieve this by using the join() method on a list comprehension that extracts the keys from the dictionary.
    def __str__(self):
        return f'MySet: {{{",".join(str(value) for value in self.dictionary)}}}'