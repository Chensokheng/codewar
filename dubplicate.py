
from collections import Counter

def duplicate_encode(word):
    print(Counter(word))
    ans = ""
    for ele in word:
        if word.count(ele) >  1:
            ans += ")"
        else:
            ans += "("
    return(ans)    
    
    #your code here

print(duplicate_encode("eabacc"))