import queue

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        def isOverlapping(a, b):
            if a[0] < b[0] and (a[1] > b[0] or a[1] > b[1]):
                return True
            if a[]

        i = 0
        while (i < len(intervals)):
            remaining = intervals[0:i] + intervals[i+1:len(intervals)]
            j = 0
            for j in range(len(remaining)):
                if intervals[i][0]


intervals = [1,2,3,4,5]
print(intervals[0:2] + intervals[3:len(intervals)])

