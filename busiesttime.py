def find_busiest_period(data):
    count = 0
    highest = 0
    currenttime = None
    result = None
    for d in data:
        if currenttime != d[0]:
            if (count > highest):
                highest = count
                result = currenttime
            currenttime = d[0]
        count += d[1] if d[2] == 1 else -d[1]
    return result


#print(find_busiest_period([[1487799426, 21, 1]]))

s = "abcd"
print(s)
print(s[0])
print(s[0:0])
print(s[0:2])
L = []
L.sort()
