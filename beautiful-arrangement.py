class Solution:
    def constructArray(self, n, k):
        ans = list(range(1, n - k))
        for i in range(k+1):
            if i % 2 == 0:
                ans.append(n-k + i//2)
            else:
                ans.append(n - i//2)

        return ans

if __name__ == "__main__":
    solution = Solution()
    print("5 1 - " + str(solution.constructArray(5,1)))
    print("5 2 - " + str(solution.constructArray(5, 2)))
    print("5 3 - " + str(solution.constructArray(5, 3)))
    print("5 4 - " + str(solution.constructArray(5, 4)))

    for i in range(1, 5):
        print(i)