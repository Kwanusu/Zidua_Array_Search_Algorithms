arr = [2, 3, 4, 10, 40]

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found at index i
    return -1  # Target not found
print(arr[3])

# Python3 code to linearly search x in arr[].


def search(arr, N, x):

    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    N = len(arr)

    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)


# Time and Space Complexity of Linear Search Algorithm:
# Time Complexity:

# Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)
# Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which 
# the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.
# Average Case: O(N)
# Auxiliary Space: O(1) as except for the variable to iterate through the list, no other variable is used. 

# Applications of Linear Search Algorithm:
# Unsorted Lists: When we have an unsorted array or list, linear search is most commonly used to find any element in 
# the collection.
# Small Data Sets: Linear Search is preferred over binary search when we have small data sets with
# Searching Linked Lists: In linked list implementations, linear search is commonly used to find elements within the list. 
# Each node is checked sequentially until the desired element is found.
# Simple Implementation: Linear Search is much easier to understand and implement as compared to Binary Search or Ternary
# Search.
# Advantages of Linear Search Algorithm:
# Linear search can be used irrespective of whether the array is sorted or not. It can be used on arrays of any data type.
# Does not require any additional memory.
# It is a well-suited algorithm for small datasets.
# Disadvantages of Linear Search Algorithm:
# Linear search has a time complexity of O(N), which in turn makes it slow for large datasets.
# Not suitable for large arrays.
# When to use Linear Search Algorithm?
# When we are dealing with a small dataset.
# When you are searching for a dataset stored in contiguous memory.
# Frequently Asked Questions (FAQs) on Linear Search Algorithm:
# 1. What is linear search algorithm?
# Linear search algorithm, also known as sequential search algorithm, is a simple searching algorithm that traverses a 
# list or array sequentially to find a target element. In Linear Search, we can get the 


# 2. How does linear search algorithm work?
# Linear search algorithm iterates through each element in the list or array, comparing it with the target element until 
# a match is found or the end of the list is reached. If the end of the list is reached, then it means that the target 
# element is not present in the array.


# 3. What is the time complexity of linear search algorithm?
# The time complexity of linear search algorithm is O(n), where n is the number of elements in the list or array being 
# searched. This means the time taken for searching increases linearly with the size of the input.


# 4. When is linear search algorithm preferred over other searching algorithms?
# Linear search algorithm is preferred when the list or array is unsorted, or when the size of the input is relatively 
# small. It’s simple to implement and doesn’t require the data to be in any specific order.


# 5. What are the advantages of linear search algorithm?
# Linear search algorithm is easy to implement, and it works efficiently on small-sized arrays or lists. It doesn’t 
# require any pre-processing like sorting, making it suitable for dynamic data structures.


# 6. What are the disadvantages of linear search algorithm?
# Linear search algorithm becomes inefficient for large-sized arrays or lists, as it needs to scan through each element 
# sequentially. It has a time complexity of O(n), which means the search time grows linearly with the size of the input.


# 7. How do you implement linear search algorithm in programming languages like Python, Java, or C++?
# Linear search algorithm can be implemented using loops to iterate through the elements of the array or list, comparing 
# each element with the target value until a match is found or the end of the list is reached.


# 8. Can linear search algorithm be applied to other data structures?
# Yes, linear search algorithm can be applied not only to arrays or lists but also to other linear data structures like 
# linked lists. The principle remains the same: iterating through each element until the target is found or the end is reached.


# 9. Is linear search algorithm suitable for sorted arrays or lists?
# While linear search algorithm can still be used on sorted arrays or lists, it’s not the most efficient option. 
# Binary search, for example, is more suitable for sorted data as it has a time complexity of O(log n).


# 10. What are some real-world applications of linear search algorithm?
# Linear search algorithm can be used in scenarios such as searching for a specific value in a phone book, 
# searching for a name in an unsorted list of contacts, or finding an item in a grocery list. It’s often used in 
# scenarios where the data size is small or not expected to grow significantly.