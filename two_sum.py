"""
Given a sorted array of integers, return the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution
and you may not use the same element twice.
"""

A = [-2,1,2,4,7,11]
target = 13

# brute force approach
# Time complexity: O(n^2)
# Space complexity: O(1)
def two_sum_brute(A, target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print A[i], A[j]
                return True
    return False

print(two_sum_brute(A, target))

# hash table approach
# H(x) = [target - x]
# Time complexity: O(n)
# Space complexity: O(n)
def two_sum_hash(A, target):
    ht = dict()
    for i in range(len(A)-1):
        if A[i] in ht:
            print A[i], ht[A[i]]
            return True
        ht[target - A[i]] = A[i]
    return False


print(two_sum_brute(A, target))

# Time complexity: O(n)
# Space complexity: O(1)
def two_sum(A, target):
    i = 0
    j = len(A)-1
    while i<=j:
        if A[i] + A[j] == target:
            print A[i], A[j]
            return True
        elif A[i] + A[j] < target:
           i+=1
        else:
            j-=1
    return False

print(two_sum_brute(A, target))
