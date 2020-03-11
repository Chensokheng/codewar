# https: // www.codewars.com/kata/541c8630095125aba6000c00/train/python
# def digital_root(n):
#     temp = 0
#     if n // 10 == 0:
#         return n
#     while n != 0:
#         last = n % 10
#         temp += last
#         n = n//10
#     return digital_root(temp)
# ...


# print(digital_root(16))


def digital_root(n):
    return n % 9 or n and 9


print(digital_root(6))
