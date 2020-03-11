from collections import Counter
def duplicate_count(text):
    if not text:
        return 0
    dict_letter = Counter(text)
    return len([ele for ele in dict_letter.keys() if dict_letter[ele] > 1])
    # Your code goes here
     

print(duplicate_count("Indivisibilities"))


    # print(max(dict_letter,key=dict_letter.get))
