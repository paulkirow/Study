import heapq
import sys


class Solution:
    def cutOffTree(self, forest: [[int]]) -> int:
        # Get order to visit nodes
        order = []
        for y in range(len(forest)):
            for x in range(len(forest[y])):
                heapq.heappush(order, (forest[y][x], (y, x)))

        total_distance = 0
        source = (0, 0)
        while len(order) > 0:
            dest = heapq.heappop(order)

            this_dist = forest_dijkstras(forest, source, dest[1])
            source = dest
            if this_dist == -1:
                return -1
            total_distance += this_dist

        return total_distance


def forest_dijkstras(forest: [[int]], source, dest):
    dist_map = {}
    for y in range(len(forest)):
        dist_map.update({(x, y): sys.maxsize for x in range(len(forest[y]))})
    visited = {}
    dist_map[source] = 0
    while len(visited) < len(forest) * len(forest[0]):
        current = __min_dist(dist_map, visited)
        if current == dest:
            return dist_map[current]
        visited[current] = True
        for e in get_edges(current):
            if valid_edge(e, forest):
                dist_map[e] = min(dist_map[e], dist_map[e] + dist_map[current])

    return -1


def valid_edge(tuple, forest):
    return 0 <= tuple[0] < len(forest[0]) and 0 <= tuple[1] < len(forest) and forest[tuple[0]][tuple[1]] != 0


def get_edges(tuple):
    left = (tuple[0] - 1, tuple[1])
    right = (tuple[0] + 1, tuple[1])
    up = (tuple[0], tuple[1] - 1)
    down = (tuple[0], tuple[1] + 1)
    return [left, right, up, down]


def __min_dist(dist_map, visited_map):
    min_index = None
    min = sys.maxsize
    for v in dist_map.keys():
        if dist_map[v] < min and v not in visited_map:
            min = dist_map[v]
            min_index = v
    return min_index


if __name__ == '__main__':
    forest = [
        [1, 2, 3],
        [0, 0, 4],
        [7, 6, 5]
    ]
    solution = Solution()

    print(solution.cutOffTree(forest))
