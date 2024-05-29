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


print(generateMatrix(3))
#[[1,2,3],
# [8,9,4],
# [7,6,5]]
print(generateMatrix(4))
#  [[1, 2, 3, 4], 
# [12, 13, 14, 5], 
# [11, 16, 15, 6], 
#  [10, 9, 8, 7]]