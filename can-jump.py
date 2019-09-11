import queue


class Solution:
    def canJump(self, nums: [int]) -> bool:
        def canJumpDFS(items, index = 0) -> bool:
            if not items:
                return False
            if items[0] == 0:
                print("-- 0 --")
                return False
            if len(items) == 1:
                return True
            for i in range(items[0], 0, -1):
                print(str(items[0])+":" + str(i)+" -> "+str(i+index) + "  " + str(nums[0:index]) + str(items[0:i])+ str(items[i:]))
                if canJumpDFS(items[i:], i+index):
                    return True
            return False

        def canJumpBFS(items) -> bool:

            if not items:
                return False
            destination = len(items) - 1
            visited = {}
            q = queue.Queue()
            q.put(0)

            while not q.empty():
                index = q.get()
                visited[index] = True
                if index >= destination:
                    return True
                for i in range(items[index], 0, -1):
                    next_index = index + i
                    if next_index not in visited:
                        q.put(next_index)

            return False

        def canJumpFromPosition(position, nums):
            if position == len(nums) - 1
                return True

            furthestJump = min(position + nums[position], len(nums) - 1);
            for nextPosition in range(position + 1, furthestJump + 1) {
            if canJumpFromPosition(nextPosition, nums)
            return True

            return False

        return canJumpBFS(nums)

if __name__ == "__main__":
    input = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    #input = [2,3,1,1,4]
    solution = Solution()

    print(solution.canJump(input))