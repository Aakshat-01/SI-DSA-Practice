# Given an unsorted array arr[] of size n, 
# containing elements from the range 1 to n, 
# it is known that one number in this range is missing, 
# and another number occurs twice in the array, 
# find both the duplicate number and the missing number.


class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        duplicate = missing = -1
        for i in range(1, n+1):
            if i not in freq:
                missing = i
            elif freq[i] == 2:
                duplicate = i
        return [duplicate, missing]