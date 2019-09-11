class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        m_len = len(matrix)
        n_len = len(matrix[0])
        m = n = buffer = 0
        direction = 'r'
        output = []
        for i in range(m_len * n_len):
            print("["+str(m)+"]["+str(n)+"]")
            output.append(matrix[m][n])

            if direction == 'r':
                if n >= n_len - buffer - 1:
                    direction = 'd'
                else:
                    n += 1

            if direction == 'd':
                if m >= m_len - buffer - 1:
                    direction = 'l'
                else:
                    m += 1

            if direction == 'l':
                if n <= buffer:
                    direction = 'u'
                    buffer += 1
                else:
                    n -= 1

            if direction == 'u':
                if m <= buffer:
                    direction = 'r'
                    n += 1
                else:
                    m -= 1

        return output

if __name__ == "__main__":
    input = [[1,2,3],[4,5,6],[7,8,9]]
    solution = Solution()

    print(solution.spiralOrder(input))