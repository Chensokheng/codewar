def persistence(n,count = 0):
    if n // 10 == 0:
        return count
    else:
        temp = 1
        while n != 0:
            temp *= n % 10
            n = n // 10
        count += 1
        return persistence(temp,count)
    # your code

print(persistence(999))