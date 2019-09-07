def repeatedString(s, n):
    if (len(s) == 0 or n == 0):
        return 0
    num_a = s.count('a')
    factor = n // len(s)
    remainder = n % len(s)
    num_a_r = s[0:remainder].count('a')
    return num_a * factor + num_a_r


if __name__ == '__main__':

    s = 'abaaa'

    n = 11

    result = repeatedString(s, n)

    print(str(result) + '\n')
