import heapq
import sys


class Solution:
    def shortestDistance(self, grid: [[int]]):
        buildings = []
        num_rows = len(grid)
        num_cols = len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                value = grid[row][col]
                if value == 1:
                    buildings.append((row, col))

        # return the distance to each building from given starting position
        def bfs(start, min_heap, visited):
            min_heap = [(0, start)]
            result = {b: sys.maxsize for b in buildings}
            visited = {}
            while len(min_heap) > 0:
                cur = heapq.heappop(min_heap)
                if cur in visited:
                    break
                visited[cur[1]] = True
                row = cur[1][0]
                col = cur[1][1]
                value = grid[row][col]
                distance = cur[0]
                if value == 1:
                    result[cur[1]] = distance
                if value == 0:
                    # Push all 4 directions to heap
                    left = (row, col - 1)
                    right = (row, col + 1)
                    up = (row - 1, col)
                    down = (row + 1, col)
                    if col - 1 >= 0 and left not in visited:
                        heapq.heappush(min_heap, (distance+1, left))
                    if col + 1 < num_cols and right not in visited:
                        heapq.heappush(min_heap, (distance + 1, right))
                    if row - 1 >= 0 and up not in visited:
                        heapq.heappush(min_heap, (distance + 1, up))
                    if row + 1 < num_rows and down not in visited:
                        heapq.heappush(min_heap, (distance + 1, down))
                #print(min_heap)
            return result
        min_dist = sys.maxsize
        min_cord = None
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != 1:
                    dist = bfs((row, col))
                    dist_val = 0
                    for key in dist.values():
                        dist_val += key
                    print(dist)
                    print((row, col), dist_val)
                    if dist_val < min_dist:
                        min_dist = dist_val
                        min_cord = (row,col)

        if min_dist >= sys.maxsize:
            return -1
        return min_dist

if __name__=="__main__":
    grid = [[1, 0, 2, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]]
    grid = [[1]]
    grid = [[1, 1], [0, 1]]
    grid = [[2, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 2, 0, 1, 1, 0],
     [0, 1, 0, 1, 1, 2, 0, 0, 2, 0, 0, 2, 0, 2, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2],
     [0, 0, 2, 2, 2, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0],
     [0, 2, 0, 2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 1],
     [0, 0, 2, 1, 2, 0, 2, 0, 0, 0, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 2, 0],
     [0, 0, 0, 2, 1, 2, 0, 0, 2, 2, 2, 1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 1, 1],
     [0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 2, 0, 2, 2, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0],
     [2, 0, 2, 0, 0, 0, 2, 0, 2, 2, 0, 2, 0, 0, 2, 0, 0, 2, 1, 0, 0, 0, 2, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 0, 2, 2, 0, 0, 2, 2]]
    solution = Solution()
    print(solution.shortestDistance(grid))