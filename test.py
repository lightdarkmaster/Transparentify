def separateCharAndNum(str):
    char = []
    num = []
    for i in str:
        if i.isalpha():
            char.append(i)
        else:
            num.append(i)
    return char, num
print(separateCharAndNum("test123"));