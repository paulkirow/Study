class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = ""
        word = ""
        for i in range(len(s)):

            if s[i] == " ":
                new_s += word + " "
                word = ""
            else:
                word = s[i] + word
        return new_s + word
solution = Solution()

print(solution.reverseWords("Let's take LeetCode contest"))
