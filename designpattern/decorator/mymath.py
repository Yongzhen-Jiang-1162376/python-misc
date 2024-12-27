known_sum = {0:0}

def nsum(n):
    assert(n >= 0), 'n must be >= 0'
    if n in known_sum:
        return known_sum[n]
    res = n + nsum(n - 1)
    known_sum[n] = res
    return res

print(nsum(200))
