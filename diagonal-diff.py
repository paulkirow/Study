def diagonalDifference(arr):
    rows = len(arr)
    rd = 0
    ld = 0
    print(arr)
    # Write your code here
    for i in range(0,rows):
        rd+=arr[i][i]
        ld+=arr[rows - i -1][i]
    return abs(rd - ld)

def timeConversion(s):
    #
    # Write your code here.
    #
    n = len(s)
    if s[n - 2: n] == 'PM':
        return str(int(s[0:2])+12)+s[2:n-2]
    else:
        return s[0:n-2]

if __name__ == '__main__':

    n = 3

    arr = []

    arr.append(list(map(int, '11 2 4'.rstrip().split())))
    arr.append(list(map(int, '4 5 6'.rstrip().split())))
    arr.append(list(map(int, '10 8 -12'.rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')

    arr = [1,2,3,4,5]
    print(arr[0:3])

    print(timeConversion('12:40:22AM'))