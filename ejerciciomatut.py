def sum_mul(n, m):
    if n == 0 or m == 0:
        return "INVALID"
    elif m % n == 0 and n < m and n > 0 and m > 0:
        return n*m
    elif n == m:
        return 0
    elif n > m and n > 0 and m > 0:
        return 0
    else:
        return "INVALID"
    
print(sum_mul(2,10))