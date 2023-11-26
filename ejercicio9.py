def sum_mul(n, m):
    
    if n == 0 or m == 0:
        return "INVALID"
    elif n <= 0 or m <= 0:
        return "INVALID"
    elif n == 0 or n > m:
        return 0
    sumyx = []
    for num in range(n, m): 
        if m % n == 0: # EL chat me dice que se suman los numeros pero no veo el como 
            sumyx.append(num)

    return sum(sumyx)
                

print(sum_mul(2,4))