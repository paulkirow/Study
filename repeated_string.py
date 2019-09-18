def repeatedString(s, n):
    if (len(s) == 0 or n == 0):
        return 0
    num_a = s.count('a')
    factor = n // len(s)
    remainder = n % len(s)
    num_a_r = s[0:remainder].count('a')
    return num_a * factor + num_a_r


def isPalindrome(s):
    j = (len(s) - 1) // 2
    i = j + (1 - len(s) % 2)
    while j >= 0 and i < len(s) and s[j] == s[i]:
        j -= 1
        i += 1

    return j == -1 and i == len(s)


def longestPalindrome(s: str) -> str:
    def p(l, r):
        if l > r:
            return 0
        if l == r:
            return 1

        if s[l] == s[r]:
            return p(l + 1, r - 1) + 2

        return max(p(l + 1, r), p(l, r - 1))

    return p(0, len(s) - 1)


def convert(s: str, numRows: int) -> str:
    result = ""
    for i in range(len(s)):
        new_i = (i % numRows) + (i // numRows)
        result += s[new_i]
    return result


def myAtoi(str: str) -> int:
    substring = str
    digits = []
    multiple = 1
    seen_digit = False
    is_bad = False
    result = 0
    while len(substring) > 0:
        if substring[0] == ' ' or substring[0] == '+':
            substring = substring[1:]
        elif substring[0] == '-':
            multiple = 1
            substring = substring[1:]
        elif substring[0] in "1234567890":
            digits.append(int(substring[0]))
            seen_digit = True
            substring = substring[1:]
        elif seen_digit:
            break
        else:
            is_bad = True

    for i in range(digits):
        digit = digits[i]
        result += digit * (len(digits) - i)

    if not is_bad:
        return result * multiple


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val) + " -> " + str(self.next)

    @staticmethod
    def initFromList(list):
        if len(list) == 0:
            return None
        result = ListNode(list[0])
        if len(list) == 1:
            return result
        result.next = result.initFromList(list[1:])
        return result


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 == None:
        return l2
    if l2 == None:
        return l1
    result = l1
    l1_t = ListNode(0)
    l1_t.next = l1
    l1 = l1_t
    l2_t = ListNode(0)
    l2_t.next = l2
    l2 = l2_t
    while l1.next is not None or l2.next is not None:
        l1_n = l1.next
        l2_n = l2.next
        if l1_n is None:
            l1.next = l2.next
            l2.next = None
        elif l2_n is None:
            return result
        elif l1_n.val <= l2_n.val:
            l1 = l1.next
        elif l1_n.val > l2_n.val:
            new_node = ListNode(l1_n.val)
            new_node.next = l1_n.next
            l1_n.val = l2_n.val
            l1_n.next = new_node
            l2.next = l2_n.next
            l1 = l1.next

    return result


def permute(nums: [int]) -> [[int]]:
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [nums]
    elif len(nums) == 2:
        return [nums, [nums[1],nums[0]]]

    subset = permute(nums[1:])

    result = []

    for p in subset:
        for i in range(len(p)+1):
            x = p[0::]
            x.insert(i, nums[0])
            result.append(x)

    return result

def firstMissingPositive(nums: [int]) -> int:
    if not nums:
        return 1
    elif len(nums) == 1:
        if nums[0] == 1:
            return 2
        else:
            return 1

    i = 0
    while i < len(nums):
        if nums[i] > len(nums) or nums[i] <= 0:
            nums[i] = len(nums) + 2
        i += 1

    i = 0
    while i < len(nums):
        if abs(nums[i]) - 1 < len(nums) and nums[abs(nums[i])-1]>0:
            nums[abs(nums[i]) - 1] *= -1
        i += 1
    print(nums)
    missing = len(nums)
    for i in range(len(nums)):
        if nums[i] <= 0 or nums[i] >= len(nums):
            missing -= 1
    return missing

if __name__ == '__main__':
    s = 'abaaa'

    n = 11

    result = repeatedString(s, n)

    print(str(result) + '\n')

    print(longestPalindrome('abba'))
    print(longestPalindrome('abababa'))
    print(longestPalindrome('a'))
    print(longestPalindrome('abc'))
    print(longestPalindrome('abbd'))
    print(longestPalindrome('abababd'))
    print(max("zz", "aaab"))

    # print(myAtoi("     -1234 abc"))

    print("abcdef"[1:-1])

    l = [4, 3, 6, 2, 1]
    print(l)
    print(l.pop())
    print(l)
    print(l.pop())
    print(l.pop())
    print(l)

    l1 = ListNode.initFromList([9, 8, 7, 6, 5, 4, 3, 2, 1])
    l2 = ListNode.initFromList([1, 2, 3, 4])
    print(mergeTwoLists(l1, l2))

    print(permute([1, 2, 3]))

    print(firstMissingPositive([-10,-3,-2,-1,0,10,11,12,2,1,5,6,7,8,9,1000,-8,-6,-4,10002,1002,100,39]))
    print(firstMissingPositive([1,2,3,4,5,6,7,8,9,10]))