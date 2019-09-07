def sherlockAndAnagrams(s):
    h = {}
    result = 0
    for i in range(0,len(s)):
        for j in range(i + 1,len(s) + 1):
            sub = ''.join(sorted(s[i:j]))
            if (sub in h):
                h[sub] = h[sub] + 1
            else:
                h[sub] = 0
    for v in h.values():
        result += v*(v+1)/2
    return int(result)

s = 'kkkk'
print(s[1:1])
result = sherlockAndAnagrams(s)

print(str(result) + '\n')