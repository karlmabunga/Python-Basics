def stringReversal(s):
    res = ''

    # Option 1:
    # for i in range(len(s) - 1, -1, -1):
    #     res += s[i]

    #Option 2:
    l = list(s)
    l.reverse()
    res = ''.join(l)

    return res


# print(stringReversal('hello') == 'olleh')
# print([c for c in "hello"])

def isPalindrome(s):
    l,r = 0, len(s) - 1
    if s[l] != s[r]:
        return False
    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

# print(isPalindrome('mom'))
# print(isPalindrome('racecar'))
# print(isPalindrome('stars'))
# print(isPalindrome('racecars'))

def reverseInt(num):
    res = 0
    if num > 0:
        sign = 1
    else: 
        sign = -1
    n = abs(num)

    while n:
        digit = n % 10
        res = res * 10 + digit
        n = int(n / 10)

    return res * sign

# print(reverseInt(-513) == -315) # True
# print(reverseInt(25929) == 92952) # True
# print(reverseInt(202) == -202) # False
# print(reverseInt(1354) == 1354) # False

def countSteps(n, row = 0, stair = ''):
    if n == row:
        return
    
    if n == len(stair):
        print(stair)
        return countSteps(n, row + 1)

    if len(stair) <= row:
        stair += '#'
    else:
        stair += ' '

    countSteps(n, row, stair)

# print(countSteps(15))

def generateMatrix(n):
    res = [[0] * n for _ in range(n)]
    counter = 1
    top, left = 0, 0
    bottom, right = n - 1, n - 1

    while top <= bottom and left <= right:
        # Top Row
        for i in range(left, right + 1):
            res[top][i] = counter
            counter += 1

        top += 1

        # Right Column
        for i in range(top, bottom + 1):
            res[i][right] = counter
            counter += 1
        right -= 1

        if top > bottom or left > right:
            break

        # Bottom Row
        for i in range(right, left - 1, -1):
            res[bottom][i] = counter
            counter += 1
        bottom -= 1

        # Left Column
        for i in range(bottom, top - 1, -1):
            res[i][left] = counter
            counter += 1
        left += 1

    
    return res


# print(generateMatrix(3))
#[[1,2,3],
# [8,9,4],
# [7,6,5]]
# print(generateMatrix(4))
#  [[1, 2, 3, 4], 
# [12, 13, 14, 5], 
# [11, 16, 15, 6], 
#  [10, 9, 8, 7]]

def spiralOrder(matrix):
    res = []
    left, right = 0, len(matrix[0]) - 1
    top, bottom = 0, len(matrix) - 1

    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            res.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            res.append(matrix[row][right])
        right -= 1

        # if left > right or bottom > top:
        #     break

        for col in range(right, left - 1, -1):
            res.append(matrix[bottom][col])
        bottom -= 1

        for row in range(bottom, top - 1, -1):
            res.append(matrix[row][left])
        left += 1

    return res

# print(spiralOrder([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]]))
# [1,2,3,6,9,8,7,4,5]
# print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
# [1,2,3,4,8,12,11,10,9,5,6,7]


def fib(n, memo = {}):
    if n < 2:
        return n
    if n in memo:
        return memo[n]
    
    res = fib(n-1, memo) + fib(n - 2, memo)
    memo[n] = res
    return res

def slowFib(n):
    if n < 2:
        return n
    return slowFib(n - 1) + slowFib(n - 2)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# print(fib(365))
# print(slowFib(35))


# Anagram Groups
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


def groupAnagrams(strs):
    res = {}

    for s in strs:
        key = [0] * 26
        for c in s:
            key[ord(c) - ord('a')] += 1
        key = tuple(key)
        if key not in res:
            res[key] = [s]
        else:
            res[key].append(s)
    return res.values()

    
# print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
# Input: strs = ["act","pots","tops","cat","stop","hat"]
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


# Top K Elements in List
# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.


def topKFrequent(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    freq = [[] for _ in range(len(nums) + 1)]
    for n, c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


# print(topKFrequent([1,1,2,2,2,3,3,3,3,3], 2))
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]
# print(topKFrequent([7,7], 1))
# Input: nums = [7,7], k = 1
# Output: [7]

################################################################################################################################################################

# Products of Array Discluding Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 𝑂(𝑛) time without using the division operation?

def productExceptSelf(nums):
    res = [1] * len(nums)
    pre = 1
    for i, n in enumerate(nums):
        res[i] = pre
        pre *= n
    post = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= post
        post *= nums[i]
    return res
    
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]
# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

print(productExceptSelf([1,2,4,6]))
print(productExceptSelf([-1,0,1,2,3]))

################################################################################################################################################################

# Longest Consecutive Sequence
# Given an array of integers nums, return the length of the longest consecutive sequence of elements.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

# You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums):
    s = set(nums)
    longest = 0
    for n in nums:
        if (n - 1) not in s:
            length = 0
            while n + length in s:
                length += 1
                longest = max(longest, length)
    return longest

# Input: nums = [2,20,4,10,3,4,5]
# Output: 4
# Input: nums = [0,3,2,5,4,6,1,1]
# Output: 7
print(longestConsecutive([2,20,4,10,3,4,5]))
print(longestConsecutive([0,3,2,5,4,6,1,1]))
