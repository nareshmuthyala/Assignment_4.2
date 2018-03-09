def filter_long_words(list1):
    list2 = list()
    for item in list1:
            list2.append(len(item))
    return list2

def isVowel(char):
    if len(char)==1 and char in 'aeiouAEIOU':
        return True
    return False


print(filter_long_words(["one", "to", "three","four"]))
print(isVowel('AE'))