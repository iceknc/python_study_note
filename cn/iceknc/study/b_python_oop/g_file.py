"""
操作文件流程
    1.打开文件
    2.读、写文件
    3.关闭文件
操作文件的的函数
    open  打开文件  file = open('文件路径', '访问方式')
        如果文件存在，返回文件操作对象
        如果文件不存在，抛出异常
    read  读取文件到内存中
        一次性读入并返回文件的所有内容
    readline  一次读取一行内容
    write 将指定内容写入文件
    close 关闭文件
文件指针
    标记从哪个位置开始读取数据
    第一次打开文件时，文件指针会指向文件的开始位置
    当执行了read方法后，文件指针会移动到读取内容的末尾
打开文件的方式
    r  只读方式打开文件，默认模式，如果文件不存在，会抛出异常
    w  只写方式打开文件，如果文件存在会被覆盖，如果文件不存在，会创建新文件
    a  追加方式打开文件，如果文件存在，指针将会放在文件的末尾，如果文件不存在，创建新的文件进行写入
    r+ 读写方式打开文件，文件的指针会放在文件的开头，文件不存在则抛出异常
    w+ 读写方式打开文件，文件存在会被覆盖，不存在则创建新文件
    a+ 读写方法打开文件，文件存在则文件指针放在文件的末尾，文件不存在则创建新文件写入

    频繁的移动文件指针，会影响文件的读写效率，开会中更多的时候会以只读、只写的方式来操作文件
"""

file = open("setup.py")
text = file.read()
file.close()
print(text)

file = open("setup.py")
while True:
    text = file.readline()
    if not text:
        break
    print(text)
file.close()

file = open("__init__.py", "a")
file.write("\n\n\n\n#file write test")
file.close()

#小文件复制 大文件用行读取
file_read = open("setup.py")
file_write= open("setup[copy].py","w")
text = file_read.read()
file_write.write(text)
file_read.close()
file_write.close()

