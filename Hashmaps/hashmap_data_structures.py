#  Hash Map in Python

#  Hash maps are indexed data structures. A hash map makes use of a hash function to compute an index with a key into an 
#  array of buckets or slots. Its value is mapped to the bucket with the corresponding index. The key is unique and 
# immutable. Think of a hash map as a cabinet having drawers with labels for the things stored in them. For example, 
# storing user information- consider email as the key, and we can map values corresponding to that user such as the 
# first name, last name etc to a bucket.  

#  Hash function is the core of implementing a hash map. It takes in the key and translates it to the index of a bucket in 
#  the bucket list. Ideal hashing should produce a different index for each key. However, collisions can occur. 
# When hashing gives an existing index, we can simply use a bucket for multiple values by appending a list or by rehashing.

#  In Python, dictionaries are examples of hash maps. We'll see the implementation of hash map from scratch in order to learn
#   how to build and customize such data structures for optimizing search.

#  The hash map design will include the following functions:

#  set_val(key, value): Inserts a key-value pair into the hash map. If the value already exists in the hash map, update the 
#  value.
#  get_val(key): Returns the value to which the specified key is mapped, or “No record found” if this map contains no mapping
#   for the key.
#  delete_val(key): Removes the mapping for the specific key if the hash map contains the mapping for the key.
#  Below is the implementation.



class HashTable:

    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # Insert values into hash map
    def set_val(self, key, val):
      
        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # Return searched value with specific key
    def get_val(self, key):
      
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            # check if the bucket has same key as 
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):
      
        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return

    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = HashTable(50)

# insert some values
hash_table.set_val('gfg@example.com', 'some value')
print(hash_table)
print()

hash_table.set_val('portal@example.com', 'some other value')
print(hash_table)
print()

# search/access a record with key
print(hash_table.get_val('portal@example.com'))
print()

# delete or remove a value
hash_table.delete_val('portal@example.com')
print(hash_table)
#  Output:



#  Time Complexity:

#  Memory index access takes constant time and hashing takes constant time. Hence, the search complexity of a hash map is 
#  also constant time, that is, O(1).

#  Advantages of HashMaps



#  ● Fast random memory access through hash functions 

#  ● Can use negative and non-integral values to access the values. 

#  ● Keys can be stored in sorted order hence can iterate over the maps easily.

#  Disadvantages of HashMaps 

#  ● Collisions can cause large penalties and can blow up the time complexity to linear. 

#  ● When the number of keys is large, a single hash function often causes collisions. 

#  Applications of HashMaps 

#  ● These have applications in implementations of Cache where memory locations are mapped to small sets. 

#  ● They are used to index tuples in Database management systems. 

#  ● They are also used in algorithms like the Rabin Karp pattern matching

#  Hash Map in Python – FAQs
#  What Defines a Hash Map in Python?
#  A hash map (or hash table) in Python is a data structure that provides fast access to values associated with unique keys. 
#  It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found. 
#  Python’s built-in dict type is an implementation of a hash map.


#  How to Implement a Hash Map with Python Dictionaries?
#  Python dictionaries are the standard way to implement hash maps. They provide an efficient way to store and retrieve 
#  data based on keys.


#  Example:


#  # Creating a hash map (dictionary)
hash_map = {}

# Adding key-value pairs
hash_map["name"] = "Alice"
hash_map["age"] = 25
hash_map["city"] = "New York"

# # Accessing values
print(hash_map["name"])  # Output: Alice
print(hash_map["age"])   # Output: 25

# Modifying values
hash_map["age"] = 26

# Removing key-value pairs
del hash_map["city"]

# Checking for keys
if "name" in hash_map:
    print("Name is in the hash map")
#  What Are Key Differences Between Hash Maps and Lists in Python?
#  Hash Maps (Dictionaries):


#  Access Time: Average O(1) time complexity for lookups, insertions, and deletions.
#  Key-Value Pairs: Stores data as key-value pairs.
#  Order: Maintains insertion order (from Python 3.7 onwards).
#  Usage: Ideal for fast lookups based on unique keys.
#  Lists:


#  Access Time: O(1) time complexity for accessing elements by index; O(n) for searching by value.
#  Sequential Data: Stores ordered, sequential data.
#  Order: Maintains order of elements.
#  Usage: Ideal for ordered collections and sequential access.
#  How to Manage Collisions in Python Hash Maps?
#  Python’s dictionaries handle collisions using a technique called open addressing with quadratic probing. 
#  When two keys hash to the same index, the dictionary searches for the next available slot using a defined probing sequence.


#  Example:


#  # Handling collisions is managed internally by Python's dictionary implementation.
#  # Users do not need to handle collisions explicitly.
#  hash_map = {"key1": "value1", "key2": "value2"}
#  What Are the Performance Benefits of Using Hash Maps in Python?
#  Fast Access: Hash maps provide average O(1) time complexity for lookups, insertions, and deletions, making them highly 
#  efficient for 
#  these operations.
#  Efficient Memory Usage: Hash maps dynamically resize to maintain efficient usage of memory.
#  Easy Management: Python’s built-in dictionary type abstracts away the complexities of hash map implementation, including 
#  collision management and resizing.
#  Versatile: Can store heterogeneous data and different types of keys and values.
#  Order Preservation: From Python 3.7 onwards, dictionaries maintain the insertion order, providing an added benefit for 
#  ordered data access.

#  Duration: 2 hours
#  Lesson Outline
#  Introduction to Hashmaps (20 mins)

#  Definition: Explain what a hashmap is — a data structure that maps keys to values, enabling fast data retrieval.
#  Real-world Analogies: Use real-life examples, like a dictionary (word to definition) or a phone book (name to phone number).
#  Key Characteristics:
#  Constant time complexity: Explain how hashmaps can perform lookups, insertions, and deletions in constant time, on average.
#  Key-value pairs: Introduce the concept of key-value pairs and discuss why they are useful.
#  Examples: Briefly discuss typical use cases, such as counting items, caching, and managing unique items.
#  How Hashmaps Work Internally (30 mins)

#  Hash Function:
#  Explain what a hash function is and its role in transforming keys into indices for array storage.
#  Properties of a good hash function: Consistency, uniform distribution, and efficiency.
#  Collision Handling:
#  Collisions: Explain why they happen (different keys can have the same hash).
#  Collision Resolution Techniques:
#  Chaining: Explain with a visual diagram and pseudocode. Show how linked lists can be used to handle collisions at the same index.
#  Open Addressing: Briefly introduce probing techniques like linear probing and quadratic probing.
#  Load Factor:
#  Define load factor and how it affects performance.
#  Explain the concept of resizing (rehashing) and when it’s triggered.
#  Hands-on Coding Exercise: Basic Hashmap Implementation (25 mins)

#  Guide students through implementing a simple hashmap in a chosen programming language.
#  Structure of Implementation:
#  Define an array to store values.
#  Write a hash function.
#  Implement insertion and retrieval methods.
#  Implement collision handling (either chaining or open addressing).
#  Walk through each part of the implementation to solidify understanding.
#  Practical Examples and Use Cases (20 mins)

#  Counting Frequency of Elements:
#  Provide an example using hashmaps to count the frequency of elements in a list.
#  Discuss how the hashmap efficiently stores counts and provides quick lookups.
#  Anagram Checker:
#  Create an example that checks if two strings are anagrams by using a hashmap to count character occurrences.
#  Caching Example (if time permits):
#  Briefly introduce the idea of caching and how hashmaps are often used to store precomputed results for fast access.
#  Common Pitfalls and Best Practices (15 mins)

#  Pitfalls:
#  Discuss the possibility of poor hash functions leading to excessive collisions and reduced performance.
#  Mention high load factors and the importance of choosing appropriate load factors to avoid frequent resizing.
#  Best Practices:
#  Always choose a reliable hash function.
#  Ensure appropriate initial capacity based on expected data volume.
#  Discuss the importance of considering thread-safety in multi-threaded environments.
#  Q&A and Recap (10 mins)

#  Answer any student questions.
#  Review key points: hash function, collision resolution, load factor, and use cases.
#  Summarize how hashmaps optimize data retrieval and storage.
#  Homework Assignment (optional)

#  Ask students to write a hashmap-based solution to a problem, such as:
#  Finding the first non-repeating character in a string.
#  Implementing a simple cache using a hashmap.

class HashMap:
    def __init__(self, size=10):
        """Initialize the hashmap with a specified size."""
        self.size = size
        self.map = [[] for _ in range(size)]  # Each bucket is initialized as an empty list

    def _hash(self, key):
        """Hash function to get the index based on the key."""
        # Basic hash function: sum of ASCII values of characters in key, mod the size of the map
        return sum(ord(char) for char in key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hashmap."""
        index = self._hash(key)  # Calculate index for the key
        # Check if the key exists and update if it does
        for pair in self.map[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, append new key-value pair
        self.map[index].append([key, value])

    def get(self, key):
        """Retrieve a value by its key from the hashmap."""
        index = self._hash(key)  # Calculate index for the key
        for pair in self.map[index]:
            if pair[0] == key:
                return pair[1]
        return None  # Return None if the key is not found

    def delete(self, key):
        """Remove a key-value pair from the hashmap."""
        index = self._hash(key)
        for i, pair in enumerate(self.map[index]):
            if pair[0] == key:
                del self.map[index][i]  # Remove the pair
                return True
        return False  # Return False if the key was not found

    def display(self):
        """Display the hashmap structure for visualization."""
        for i, bucket in enumerate(self.map):
            if bucket:
                print(f"Index {i}: {bucket}")
            else:
                print(f"Index {i}: Empty")

# Demonstration of HashMap functionality
hashmap = HashMap()

# Insert key-value pairs
hashmap.insert("apple", 5)
hashmap.insert("banana", 3)
hashmap.insert("grape", 8)
hashmap.insert("orange", 10)

# Retrieve values
print("apple:", hashmap.get("apple"))  # Output: 5
print("banana:", hashmap.get("banana"))  # Output: 3
print("cherry (not inserted):", hashmap.get("cherry"))  # Output: None

# Display the hashmap structure
print("\nHashMap Structure:")
hashmap.display()

# Delete a key and check its removal
print("\nDeleting 'banana'...")
hashmap.delete("banana")
print("banana:", hashmap.get("banana"))  # Output: None

# Display the updated hashmap structure
print("\nUpdated HashMap Structure:")
hashmap.display()
