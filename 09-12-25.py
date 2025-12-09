# 11. Find all words with length greater than 4.

def long_words(sentence):
    words = sentence.split()   # split sentence into words
    
    for w in words:
        if len(w) > 4:         # check length
            print(w)

# Test
long_words("This is a python program")



# 1. Find the longest continuous sublist whose sum is exactly K. Print that sublist.

def longest_sublist_with_sum(arr, k):
    longest = []  # store the final answer

    for i in range(len(arr)):
        total = 0
        temp = []

        for j in range(i, len(arr)):
            total += arr[j]
            temp.append(arr[j])

            if total == k:
                if len(temp) > len(longest):  # check longest
                    longest = temp.copy()
                break  # stop because sublist must be continuous

    return longest


# Test cases
print(longest_sublist_with_sum([1,2,3,4,5], 9))      # → [2,3,4]
print(longest_sublist_with_sum([4,1,2,7,3,6], 10))   # → [1,2,7]
print(longest_sublist_with_sum([5,5,5,5], 10))       # → [5,5]


# 2. Check whether a list is a palindrome.

def longest_sublist(arr, K):
    longest = []

    for i in range(len(arr)):
        total = 0
        temp = []

        for j in range(i, len(arr)):
            total += arr[j]
            temp.append(arr[j])

            if total == K and len(temp) > len(longest):
                longest = temp[:]

    return longest


# Example
print(longest_sublist([1, 2, 3, 4, 5], 9))   # Output: [2,3,4]


# 3. Insert an element at its correct position in a sorted list.


def longest_sublist(arr, k):
    best = []
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            if total == k and (j - i + 1) > len(best):
                best = arr[i:j+1]
    return best

print(longest_sublist([1,2,3,7,5], 12))   # Output: [2,3,7]


# 4. Split a list into two lists: even numbers and odd numbers.

def split_even_odd(lst):
    evens = []
    odds = []
    
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    
    return evens, odds


print(split_even_odd([1,2,3,4,5,6]))


# 5. Find all unique pairs with difference K.

def pairs_diff_k(arr, k):
    result = []
    visited = set()

    for num in arr:
        if num + k in visited:
            result.append((num, num + k))
        if num - k in visited:
            result.append((num - k, num))
        
        visited.add(num)

    return result


# Test
print(pairs_diff_k([8,5,1,4,2], 3))
# Output: [(5,8), (1,4), (2,5)]
