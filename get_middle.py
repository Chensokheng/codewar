# def get_middle(s):
#     middle = len(s) // 2
#     if len(s) % 2 == 0:
#         return s[middle - 1:middle + 1]
#     else:
#         return s[middle]
#     #your code here

# print(get_middle("testin"))



def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]