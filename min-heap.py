import heapq
import sys

dict = [(0, "a"), (5, "g"), (3, "e"), (10, "b"), (1, "z")]

heapq.heapify(dict)

print(dict)
v = heapq.heapreplace(dict, (11, "z"))
print(dict)
print(v)
print("heapq pop: " + str(heapq.heappop(dict)))


def findNumberOfLIS(nums: [int]) -> int:
    if len(nums) <= 1:
        return len(nums)
    seq_lens = {i: 0 for i in range(1, len(nums) + 1)}
    i = 0
    j = 1
    while i < j < len(nums):
        seq_lens[j - i] += 1
        if nums[j - 1] < nums[j]:
            j += 1
        else:
            i = j
            j += 1
    seq_lens[j - i] += 1

    result = 0
    for k, v in seq_lens.items():
        if v != 0:
            result = k
    return (result, seq_lens[result])


print(findNumberOfLIS([1, 3, 5, 4, 7, 8]))
print(findNumberOfLIS([2, 2, 2, 2, 2, 2]))

dict = {(1, 2): 5, (2, 1): 2}
print(dict[(1,2)])

forest = [
    [1, 2, 3],
    [0, 0, 4],
    [7, 6, 5]
]
dist_map = {}
for y in range(len(forest)):
    dist_map = {(x, y): sys.maxsize for x in range(len(forest[y]))}
visited = {}
dist_map[(0,0)] = 0
print(dist_map)
#dist_map = heapq.heapify(dist_map)

print(dist_map)



print((10 - 1) >> 2)


d = {}
d["a"]=1
d["b"]=2
print(d)
d["c"]=3
d["d"]=4
print(d)
d["1"]="a"
d["a"]="4"
print(d)