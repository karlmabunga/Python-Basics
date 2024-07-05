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

# print(productExceptSelf([1,2,4,6]))
# print(productExceptSelf([-1,0,1,2,3]))

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
# print(longestConsecutive([2,20,4,10,3,4,5]))
# print(longestConsecutive([0,3,2,5,4,6,1,1]))

################################################################################################################################################################


# Three Integer Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            if sum < 0:
                l += 1
            if sum == 0:
                res.append([nums[i],nums[l],nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Input: nums = [0,1,1]
# Output: []
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# print(threeSum([-1,0,1,2,-1,-4]))
# print(threeSum([0,0,0]))

################################################################################################################################################################

# Max Water Container

# You are given an integer array heights where heights[i] represents the height of the i bar.
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.

def maxArea(heights):
    m = 0
    l, r = 0, len(heights) - 1 
    while l < r:
    # calculate distance
        dis = r - l
    # multiply dis x min between two pillars for area
        currArea = dis * min(heights[l], heights[r])
    # update possible m
        m = max(m, currArea)
    # update pointers
        if heights[l] > heights[r]:
            r -= 1
        else:
            l += 1
    return m


# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36
# Input: height = [2,2,2]
# Output: 4
# print(maxArea([1,7,2,5,4,7,3,6]))
# print(maxArea([2,22,2]))

################################################################################################################################################################

# Buy and Sell Crypto

# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

def maxProfit(prices):
    prof = 0
    l, r = 0, 1

    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
        elif prices[r] > prices[l]:
            prof = max(prof, prices[r] - prices[l])
        r += 1

    return prof
# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Input: prices = [10,8,7,5,2]
# Output: 0
# Input: prices = [5,1,5,6,7,1,10]
# Output: 9
# print(maxProfit([10,1,5,6,7,1]))
# print(maxProfit([10,8,7,5,2]))
# print(maxProfit([5,1,5,6,7,1,10]))

################################################################################################################################################################

# Longest Substring Without Duplicates
# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.


def lengthOfLongestSubstring(s) -> int:
        hashset = set()
        res = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, (r - l) + 1)
            r += 1
        
        return res

# Input: s = "zxyzxyz"
# Output: 3
# Input: s = "xxxxx"
# Output: 1

# print(lengthOfLongestSubstring("zxyzxyz"))
# print(lengthOfLongestSubstring("xxxxx"))

################################################################################################################################################################

# Longest Repeating Substring With Replacement
# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

def characterReplacement(s, k):
    chars = {}
    res = 0
    l = 0
    maxf = 0
    for r in range(len(s)):
        chars[s[r]] = 1 + chars.get(s[r], 0)
        maxf = max(maxf, chars[s[r]])
        while (r - l + 1) - maxf > k:
            chars[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)

    return res


# Input: s = "XYYX", k = 2
# Output: 4
# Input: s = "AAABABB", k = 1
# Output: 5
# print(characterReplacement('XXYK', 2))
# print(characterReplacement('AAABABB', 1))

################################################################################################################################################################

# Permutation String
# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
# Both strings only contain lowercase letters.

def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    matches = 0
    for i in range(len(s1Count)):
        matches += (1 if s1Count[i] == s2Count[i] else 0)
    
    l = 0
    for r in range(len(s1), len(s2)):
        if matches == 26: return True

        i = ord(s2[r]) - ord('a')
        s2Count[i] += 1
        if s2Count[i] == s1Count[i]:
            matches += 1
        elif s1Count[i] + 1 == s2Count[i]:
            matches -= 1
        
        i = ord(s2[l]) - ord('a')
        s2Count[i] -= 1
        if s2Count[i] == s1Count[i]:
            matches += 1
        elif s1Count[i] - 1 == s2Count[i]:
            matches -= 1

        l += 1

    return matches == 26
            
# Input: s1 = "abc", s2 = "lecabee"
# Output: true
# Input: s1 = "abc", s2 = "lecaabee"
# Output: false
# print(checkInclusion('abc', 'lecabee'))
# print(checkInclusion('abc', 'lecaabee'))
# print(checkInclusion('adc', 'dcda'))

################################################################################################################################################################

# Minimum Window With Characters
# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".
# You may assume that the correct output is always unique.
def minWindow(s, t):
    if len(t) > len(s): return ''
    window, countT = {}, {}
    # add letters to countT
    for i in range(len(t)):
        countT[t[i]] = 1 + countT.get(t[i], 0)

    # create left pointer and right pointer
    l = 0
    # create curCount and tarCount
    curCount, tarCount = 0, len(countT)
    # create res and resLength var
    res, resLength = [-1, -1], float('infinity')

    # iterate through the s string
    for r in range(len(s)):
        # create char var
        c = s[r]
        # add char to window
        window[c] = window.get(c, 0) + 1

        # if window[char] == countT[char]
        if c in countT and window[c] == countT[c]:
            # curCount inc
            curCount += 1

        # while curCount and tarCount are the same
            while curCount == tarCount:
                # update res and resLength if length < resLength
                if (r - l + 1) < resLength:
                    res = [l, r]
                    resLength = r - l + 1
                
                # remove left char from window
                window[s[l]] -= 1
                # if window[s[l]] < countT[s[l]]
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    # dec curCount
                    curCount -= 1
                    
                # inc l
                l += 1
    # destructure l and r
    l, r = res
    # return s[l:r+1] if resLength != float('infinity')
    return s[l:r+1] if resLength != float('infinity') else ''


    
    
# Input: s = "OUZODYXAZV", t = "XYZ"
# Output: "YXAZ"
# Input: s = "xyz", t = "xyz"
# Output: "xyz"
# Input: s = "x", t = "xy"
# Output: ""

# print(minWindow('OUZODYXAZV', 'XYZ'))
# print(minWindow('xyz', 'xyz'))
# print(minWindow('x', 'xy'))
# print(minWindow('acvawfsfdafsdffsd', 'aa'))

################################################################################################################################################################

# Sliding Window Maximum
# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.
# Return a list that contains the maximum element in the window at each step.

def maxSlidingWindow(nums, k):
    res = []
    l = 0

    # Brute force approach
    for r in range(k - 1, len(nums)):
        n = -float('infinity')
        for i in range(l, r + 1):
            n = max(n, nums[i])
        res.append(n)
        l += 1
    return res


# Input: nums = [1,2,1,0,4,2,6], k = 3
# Output: [2,2,4,4,6]
# Explanation: 
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6

# print(maxSlidingWindow([1,2,1,0,4,2,6], 3))
# print(maxSlidingWindow([1,-1], 1))

################################################################################################################################################################
# 2062. Count Vowel Substrings of a String

# A substring is a contiguous (non-empty) sequence of characters within a string.
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.
# Given a string word, return the number of vowel substrings in word.

def countVowelSubstrings(word):
    vowels = set("aeiou")
    count = 0

    # Brute Force Solution
    for i in range(len(word)):
        s = set()
        if word[i] in vowels:
            for j in range(i, len(word)):
                if word[j] in vowels:
                    s.add(word[j])
                    if s == vowels:
                        count += 1
                else:
                    break

    return count


# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows:
# - "aeiou"
# - "aeiouu"
# print(countVowelSubstrings('aeiouu'))

################################################################################################################################################################

# Validate Parentheses

# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

def isValid(s):
    pairs = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    stack = []
    for c in s:
        if c in pairs:
            if stack and pairs[c] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False

# Input: s = "[]"
# Output: true
# Input: s = "([{}])"
# Output: true
# Input: s = "[(])"
# Output: false
# print(isValid('[]'))
# print(isValid("([{}])"))
# print(isValid('[(])'))


################################################################################################################################################################


# Minimum Stack
# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in O(1) time.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.stack[-1] if len(self.stack) else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


################################################################################################################################################################


# Evaluate Reverse Polish Notation

# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.
# The operands may be integers or the results of other operations.
# The operators include '+', '-', '*', and '/'.
# Assume that division between integers always truncates toward zero.

def evalRPN(tokens):
    stack = []
    for t in tokens:
        if t == '+':
            stack.append(stack.pop() + stack.pop())
        elif t == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif t == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        elif t == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(t))
    return stack[0]



# print(evalRPN(["1","2","+","3","*","4","-"]))
# Input: tokens = ["1","2","+","3","*","4","-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5


################################################################################################################################################################


# (Backtrack problem)
def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(openN, closeN):
        if openN == closeN == n:
            res.append("".join(stack))
        
        if openN < n:
            stack.append('(')
            backtrack(openN + 1, closeN)
            stack.pop()
        
        if closeN < openN:
            stack.append(')')
            backtrack(openN, closeN + 1)
            stack.pop()
    
    backtrack(0, 0)
    return res


# Input: n = 1
# Output: ["()"]
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# print(generateParenthesis(1))
# print(generateParenthesis(3))
# print(generateParenthesis(2))

################################################################################################################################################################


# Daily Temperatures
# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

# Stack problem
def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            temp, idx = stack.pop()
            res[idx] = i - idx
        stack.append([t, i])
    
    return res

# Input: temperatures = [30,38,30,36,35,40,28]
# Output: [1,4,1,2,1,0,0]
# Input: temperatures = [22,21,20]
# Output: [0,0,0]
# print(dailyTemperatures([30,38,30,36,35,40,28]))
# print(dailyTemperatures([22,21,20]))


################################################################################################################################################################


# Car Fleet
# There are n cars traveling to the same destination on a one-lane highway.
# You are given two arrays of integers position and speed, both of length n.
# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.
# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
# Return the number of different car fleets that will arrive at the destination.

# time O(N log N)
# space O(N)
def carFleet(target, position, speed):
    # zip cars
    cars = [[p,s] for p, s in zip(position, speed)]
    # use stack
    stack = []

    #iterate through sorted descending position
    for p, s in sorted(cars)[::-1]:
        # push time to target to the stack
        stack.append(float(target - p) / s)
        # if two in stack and top of stack time is faster then 2nd in stack
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            # then we know it catches up to the car in front and becomes one fleet so we can pop from stack
            stack.pop()
    # return stack length (fleets)
    return len(stack)

# Input: target = 10, position = [1,4], speed = [3,2]
# Output: 1
# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.
# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]
# Output: 3
# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.


# print(carFleet(10, [1,4], [3,2]))
# print(carFleet(10, [4,1,0,7], [2,2,1,1]))
print(carFleet(10, [6,8], [3,2]))


################################################################################################################################################################


# Largest Rectangle In Histogram

# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
# Return the area of the largest rectangle that can be formed among the bars.
# Note: This chart is known as a histogram.

def largestRectangleArea():
    pass


# Input: heights = [7,1,7,2,2,4]
# Output: 8
# Input: heights = [1,3,7]
# Output: 7
# print(largestRectangleArea([7,1,7,2,2,4]))
# print(largestRectangleArea([1,3,7]))