hash_table = [[] for _ in range(10)]
print("hash_table: " + str(hash_table))


def hashing_func(key):
    return hash(key) % len(hash_table)


print("hashing_func(0): " + str(hashing_func(0)))
print("hashing_func(0): " + str(hashing_func(1)))
print("hashing_func(0): " + str(hashing_func(10)))


# def insert(hash_table, key, value):
#     hash_key = hashing_func(key)
#     hash_table[hash_key] = value

def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    bucket = hash_table[hash_key]
    ins = True
    for k, v in bucket:
        if (k == key):
            ins = False
            break
    if ins:
        hash_table[hash_key].append((key, value))


def search(hash_table, key):
    bucket = hash_table[hashing_func(key)]
    for k, v in bucket:
        if (k == key):
            return v
    return ''


def delete(hash_table, key):
    bucket = hash_table[hashing_func(key)]
    for i, kv in enumerate(bucket):
        k, v = kv
        if (k == key):
            del bucket[i]


insert(hash_table, 0, 'CAN')
insert(hash_table, 1, 'US')
insert(hash_table, 10, 'MEX')

print("hash_table: " + str(hash_table))

print("search(0): " + search(hash_table, 0))
print("search(10): " + search(hash_table, 10))
print("search(1): " + search(hash_table, 1))
print("search(11): " + search(hash_table, 11))

delete(hash_table, 1)
delete(hash_table, 10)
delete(hash_table, 0)
print("hash_table: " + str(hash_table))
