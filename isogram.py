def is_isogram(string):
    check = string
    string = set(string)
    return len(check) == len(string)
    #your code here

is_isogram("aaaaa")