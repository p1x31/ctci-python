
""" 
1.Compute the key's hash code. Two different keys can have the same hash code
2. map the hash code to an index in the array 
hash(key) % array_length
3. linked list of keys and values at the index

compute key-> hash code -> index

collisions O(N) lookup time O(1)
"""
hash_table = [None] * 10
print (hash_table) 
# Output: 
# [None, None, None, None, None, None, None, None, None, None]

def hashing_func(key):
	return key % len(hash_table)

print (hashing_func(10)) # Output: 0
print (hashing_func(20)) # Output: 0
print (hashing_func(25)) # Output: 5

assert((hashing_func(25))==5)

hash_table = [[] for _ in range(10)]

def insert(hash_table, key, value):
    hash_key = hash(key) % len(hash_table)
    key_exists = False
    bucket = hash_table[hash_key]    
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            key_exists = True 
            break
    if key_exists:
        bucket[i] =((key, value))
    else:
        bucket.append((key, value))
 
 
insert(hash_table, 10, 'Nepal')
insert(hash_table, 25, 'USA')
insert(hash_table, 20, 'India')
print (hash_table)

insert(hash_table, 10, 'Nepal')
print (hash_table)
# Output: 
# [['Nepal'], [], [], [], [], [], [], [], [], []]
 
insert(hash_table, 25, 'USA')
print (hash_table)
# Output: 
# [['Nepal'], [], [], [], [], ['USA'], [], [], [], []]
 
insert(hash_table, 20, 'India')
print (hash_table)
# Output: 
# [['Nepal', 'India'], [], [], [], [], ['USA'], [], [], [], []]


def search(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return v

def delete(hash_table, key):
    hash_key = hash(key) % len(hash_table)    
    key_exists = False
    bucket = hash_table[hash_key]
    for i, kv in enumerate(bucket):
        k, v = kv 
        if key == k:
            key_exists = True 
            break
    if key_exists:
        del bucket[i]
        print ('Key {} deleted'.format(key))
    else:
        print ('Key {} not found'.format(key))
 
print(search(hash_table, 25))

delete(hash_table, 20)
print (hash_table)
 