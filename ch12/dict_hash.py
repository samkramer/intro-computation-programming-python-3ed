# 12.3 Hash Tables
import random


# Figure 12-7 Implementing dictionaries using hashing
class Int_dict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, num_buckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.num_buckets = num_buckets
        for i in range(num_buckets):
            self.buckets.append([])
            
    def add_entry(self, key, dict_val):
        """Assumes key an int. Adds an entry."""
        # Use hash function '%' to convert key into integer
        # and use that integer to index into buckets to find
        # the hash bucket associated with key
        bucket_index = key % self.num_buckets
        hash_bucket = self.buckets[bucket_index]
        
        # Search hash bucket to see if entry exists with key
        # If key found, replace entry with new tuple
        for i in range(len(hash_bucket)):
            if hash_bucket[i][0] == key:
                hash_bucket[i] = (key, dict_val)
                return
            
        # Append new entry to hash bucket
        hash_bucket.append((key, dict_val))
        
    def get_value(self, key):
        """Assumes key an int.
           Returns value associated with key"""
        hash_bucket = self.buckets[key%self.num_buckets]
        for e in hash_bucket:
            if e[0] == key:
                return e[1]
        return None
    
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result += f'{e[0]}:{e[1]}, '
        return result[:-2] + '}' # result[:-2] omits the last comma and space


if __name__ == "__main__":
    random.seed(1) # Generate same results each run
    
    D = Int_dict(17)
    for i in range(20):
        # choose a random int in the range 0 to 10**5 - 1
        key = random.choice(range(10**5))
        D.add_entry(key, i)
        
    print('The value of the Int_dict is:')
    print(D)
    
    print()
    
    print('The buckets are:')
    for hash_bucket in D.buckets: # violates abstraction barrier
        print('  ', hash_bucket)