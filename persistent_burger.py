# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python


def persistence(n, ans=0):
    temp = 1
    if n // 10 == 0:
        return ans
    while n != 0:
        last = n % 10
        temp *= last
        n = n // 10
    ans += 1
    return persistence(temp, ans)
    # your code


print(persistence(39))
