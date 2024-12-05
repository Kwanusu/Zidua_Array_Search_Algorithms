# Lesson Plan: Hashmaps (Expanded)
# Objective
# By the end of this lesson, students should be able to:

# Understand what hashmaps are and why they’re useful, especially compared to arrays.
# Explain how hashmaps store data with keys and values.
# Implement basic operations (insertion, deletion, and lookup).
# Recognize hashing concepts (hash functions, collision handling).
# Build a hashmap from scratch.
# Apply hashmaps to solve problems.
# Duration: 2 hours
# Lesson Outline
# 1. Introduction to Hashmaps (10 minutes)
# Definition: A hashmap (or hash table) is a data structure that stores data in key-value pairs, allowing for efficient 
# retrieval based on keys.
# Usage in Programming: Primarily used for quick data retrieval, enabling fast lookups, insertions, and deletions by key.
# 2. Hashmaps vs. Arrays (15 minutes)
# Array Basics: Explain that arrays store values in contiguous memory and use integer indices to access elements in O(1) 
# time.

# Ideal for ordered data where each element has a specific position.
# Limitations: Inefficient for searching by a specific attribute (e.g., finding a value based on a key other than its 
# index).
# Why Use a Hashmap?:

# Hashmaps allow retrieval by key, making them better suited for associative data.
# Example: Looking up a phone number by name in a hashmap is much faster than in an array, where you'd need to search 
# each element sequentially.
# Performance Comparison:

# Hashmap: Average O(1) for insertion, deletion, and lookup.
# Array: O(n) for searching by key but O(1) for indexed access.
# 3. Hashing and Hash Functions (10 minutes)
# Hash Function Basics: Explain how a hash function maps keys to indices (or “buckets”) in the hashmap.
# Emphasize the importance of spreading keys uniformly across the buckets to avoid clustering.
# 4. Building a Hashmap from Scratch (40 minutes)
# Walk through the process of creating a basic hashmap class from scratch, explaining each component along the way.

# Hashmap Class Components:

# Hash Function: Converts a key into an index.
# Table Array: Stores key-value pairs at the computed indices.
# Basic Operations:
# Insert: Compute the hash index and store the key-value pair.
# Lookup: Retrieve a value by computing the index for a key.
# Delete: Remove a key-value pair based on the key.
# Step-by-Step Code Implementation:

# Here’s a Python example:

# python
# Copy code
class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Using lists for chaining
    
    def _hash(self, key):
        # A basic hash function using Python's built-in hash()
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        # Check if the key already exists in the bucket
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value  # Update value if key already exists
                return
        self.table[index].append([key, value])  # Add new key-value pair
    
    def lookup(self, key):
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]  # Return value if key found
        return None  # Return None if key not found
    
    def delete(self, key):
        index = self._hash(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]  # Remove key-value pair
                return True
        return False  # Return False if key not found
# Explanation of Code:
# Constructor (__init__): Initializes the hashmap with a list of empty lists (for separate chaining).
# Hash Function (_hash): Uses Python’s hash() and modulus to ensure indices fit within the table size.
# Insert: Checks if a key exists in the bucket before inserting to prevent duplicates.
# Lookup: Searches within the bucket to find the value for a given key.
# Delete: Removes the key-value pair if the key is found.
# 5. Collision Handling Techniques (10 minutes)
# Separate Chaining: Show how multiple values are stored in the same bucket (using lists in this example).
# Open Addressing (overview only): Briefly describe linear probing and quadratic probing for students to explore further 
# if interested.
# 6. Practical Applications and Problem-Solving (10 minutes)
# Example Use Cases:
# Counting Frequencies: Using a hashmap to count occurrences of elements.
# Finding Duplicates: Use a hashmap to check for duplicates in a list.
# Practice Problem: Find the first non-repeating character in a string using a hashmap.
# 7. Exercise and Q&A (15 minutes)
# Exercise: Extend the hashmap class to handle resizing when the load factor (items/table size) exceeds a threshold, 
# to avoid performance degradation.
# Q&A Session: Answer questions and review key concepts.