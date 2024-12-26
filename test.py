import os;

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

def renameFiles():
    path = './outputImage/'
    files = os.listdir(path);
    for i, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, f'result{i + 1}.png'));
    print("Files renamed successfully");
    

def createPath():
    path = './outputImage/'
    if not os.path.exists(path):
        os.makedirs(path);
    print("Path created successfully");
    

def removePath():
    path = './outputImage/'
    if os.path.exists(path):
        os.rmdir(path);
    print("Path removed successfully");


