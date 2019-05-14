"""
双引号或者单引号定义
    如果字符串里面需要用双引号，建议用单引号定义
    如果字符串里面需要用单引号，建议用双引号定义

string[] 取字符
len(string) 获取长度
string.count(data) 数据在字符串中出现的次数

判断类型方法
    string.isspace() 判断字符串是否只包含空格 （ \t \r \n ）
    string.isalnum() 是否至少有一个字符并且所有字符都是字母或者数字
    string.isalpha() 是否至少有一个字符并且所有的字符都是字母
    string.isdecimal() 是否只包含数字，全角数字 不能判断小数
    string.isdigit() 是否只包含数字，全角数字,(1) \u00b2 不能判断小数
    string.isnumeric() 是否只包含数字，全角数字, 汉字数字 不能判断小数
    string.istitle() 是否标题化的字符，每个单词的首字母大写
    string.islower()  是否至少包含一个区分大小写的字符，并且所有字符都是小写
    string.isupper()  是否至少包含一个区分大小写的字符，并且所有字符都是大写

查找和替换
    string.startswith(str) 是否以str开头
    string.endswith(str) 是否以str结尾
    string.find(str, start=0, end=len(string)) str是否在string中, 不在则返回-1
    string.rfind(str, start=0, end=len(string)) str是否在string中, 从右边开始找， 不在则返回-1
    string.index(str, start=0, end=len(string))  str是否在string中, 在就返回索引，不在会报错
    string.rindex(str, start=0, end=len(string))  str是否在string中，从右边开始找， 在就返回索引，不在会报错
    string.replace(old_str, new_str, num=string.count(old_str)) 替换字符串，如果num指定，则替换不超过num次

大小写替换
    string.capitalize() 第一个字母大写
    string.title  每个单词的首字母大写
    string.lower() 全部大写字母换成小写
    string.upper() 全部小写字母换成大写
    string.swapcase() 大写变小写，小写变大写

文本对齐
    string.ljust(width) 左对齐，使用空格填充至长度width, width比string的长度小则不处理
    string.rjust(width) 右对齐，使用空格填充至长度width, width比string的长度小则不处理
    string.center(width) 居中对齐，使用空格填充至长度width, width比string的长度小则不处理

去除空白符
    string.lstrip() 去除左边的空白字符
    string.rstrip() 去除右边的空白字符
    string.strip() 去除两端的空白字符

拆分和链接
    string.partition(str) 把字符串分成三个元素  str前，str，str后
    string.rpartition(str) 同上，从右边开始操作
    string.split(str="",num) 以str为分隔符切片string，如果num指定，则分隔num+1个子字符串，str默认包含 \r \t \n
    string.splitlines() 按照行 \r \n \r\n 分隔  返回一个包含各行元素的列表
    string.join(str) 以string作为分隔符，将str中所有的元素(的字符串表示)合并为一个新的字符串

字符串变量可以用 + 号拼接
字符串变量可以用 * 号重复多次
数字型变量 和 字符串 之间 不能进行其他计算 除上
"""

# 判断空字符
str = "   \r\n\t"
print(str.isspace())


# 数字判断
str1 = "435"
str2 = "⑴"
str3 = "\u00b2"
str4 = "四百一十三"
print("%s, %s, %s, %s" % (str1.isdecimal(), str1.isdigit(), str1.isnumeric(), str4.isnumeric()))
print("%s, %s, %s, %s" % (str2.isdecimal(), str2.isdigit(), str2.isnumeric(), str4.isnumeric()))
print("%s, %s, %s, %s" % (str3.isdecimal(), str3.isdigit(), str3.isnumeric(), str4.isnumeric()))

str = "abcdefg"

print(str[5])

for char in str:
    print(char)

a = "abc"
b = "efg"

print(a + b)

print(a * 5)
