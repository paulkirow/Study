class Solution:
    def checkPossibility(self, nums: [int]) -> bool:
        not_decreasing = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                not_decreasing = False
                nums.pop(i)
                nums.pop(i)
                break
        if not_decreasing:
            return True
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print("[4, 2, 1]       false - " + str(solution.checkPossibility([4, 2, 1])))
    print("[2, 3, 3, 2, 4] true  - " + str(solution.checkPossibility([2, 3, 3, 2, 4])))
    print("[4, 2, 3]       true  - " + str(solution.checkPossibility([4, 2, 3])))

