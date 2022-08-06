import os, sys

# dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, dir)

def write(bookName,Data):
    # 创建目录，open函数不会自动创建新目录
    dirPath = os.path.join(os.getcwd(), 'books')
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    filePath = os.path.join(dirPath, bookName + '.txt')

    # 此处设置字符集为utf-8，有时候gbk会有些字符不识别
    # file = open(filePath,'a+', encoding='utf-8')
    if not os.path.exists(filePath):
        file = os.open(filePath, os.O_RDWR | os.O_CREAT)
    else:
        file = os.open(filePath, os.O_RDWR | os.O_APPEND)

    file = os.open(filePath, os.O_RDWR|os.O_APPEND)
    os.write(file, bytes(Data,'UTF-8'))


