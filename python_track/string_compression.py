def strComp(chars):
    j = 0
    i = 1
    while i < len(chars):
        if chars[i] != chars[i - 1]:
            if i - j > 1:
                k = j + 1
                for l in range(len(str(i - j))):
                    chars[k] = str(i - j)[l]
                    k += 1
                
                del chars[j + 2:i]
                i = j + 3
                j = j + 2
            else:
                j += 1
                i += 1
        else:
            i += 1
    if i - j > 1:
        chars.append(i for i in (str(i-j)))
    del chars[j + 2:i]
                
    return chars



chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# print(strComp(chars))
string = ["b", "c"]
print([i for i in string])
