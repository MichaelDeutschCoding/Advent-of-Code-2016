import re
from hashlib import md5
from functools import lru_cache

trips = re.compile(r'(.)\1{2}')
salt = 'qzyelonm'

@lru_cache(maxsize=1024)
def hash_it(salt, i):
    return md5(bytes(salt + str(i), 'utf-8')).hexdigest()

def pad_keys(salt):
    found = 0
    for i in range(100000000):
        x = hash_it(salt, i)
        m = trips.search(x)
        if m:
            for j in range(i+1, i + 1001):
                y = hash_it(salt, j)
                if re.search('({})\\1\\1\\1\\1'.format(m.group(1)), y):
                    found += 1
                    if found == 64:
                        return i


#print(pad_keys('abc'))
print(pad_keys(salt))

print(hash_it.cache_info())