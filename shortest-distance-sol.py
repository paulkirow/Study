import heapq
from collections import deque


class Solution:
    def shortestDistance(self, grid: [[int]]) -> int:
        the_heap = []
        zeros, ones = self.collectOnes(grid)
        lut_node_to_count = {}
        for k in zeros:
            lut_node_to_count[k] = (0, ones.copy())
        for i in ones:
            seen = {i}
            left = (i[0], i[1] - 1)
            right = (i[0], i[1] + 1)
            up = (i[0] + 1, i[1])
            down = (i[0] - 1, i[1])
            deq = deque([left, right, up, down])
            self.rBfs(seen, grid, the_heap, deq, lut_node_to_count, i, 1, i)
        if len(the_heap) < 1:
            return -1
        return heapq.heappop(the_heap)[0]

    def rBfs(self, seen, grid, the_heap, que, lut_node_to_count, i, count, search_spot):
        deq = deque()
        for i in que:
            if -1 < i[0] < len(grid) and -1 < i[1] < len(grid[0]) and i not in seen:
                if grid[i[0]][i[1]] == 0:
                    tup = lut_node_to_count[i]
                    tup[1].remove(search_spot)
                    lut_node_to_count[i] = (tup[0] + count, tup[1])
                    if len(lut_node_to_count[i][1]) < 1:
                        heapq.heappush(the_heap, (lut_node_to_count[i][0], i))
                    seen.add(i)
                    left = (i[0], i[1] - 1)
                    right = (i[0], i[1] + 1)
                    up = (i[0] + 1, i[1])
                    down = (i[0] - 1, i[1])
                    deq.extend([left, right, up, down])
        if len(deq) > 0:
            self.rBfs(seen, grid, the_heap, deq, lut_node_to_count, i, count + 1, search_spot)
        print(lut_node_to_count)

    def collectOnes(self, grid):
        zeros = []
        ones = set()
        for k, i in enumerate(grid):
            for j, m in enumerate(i):
                if m == 0:
                    zeros.append((k, j))
                elif m == 1:
                    ones.add((k, j))
        return zeros, ones

if __name__=="__main__":
    grid = [[1, 0, 2, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    solution = Solution()
    print(solution.shortestDistance(grid))