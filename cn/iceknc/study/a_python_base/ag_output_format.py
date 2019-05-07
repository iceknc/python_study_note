"""
%s  字符串
%d  有符号十进制数 %06d 表示输出的整数显示位数， 不足的地方使用0补全
%f  浮点数  %.02f 表示显示两位小数
%%  输出 %
"""

a = "abc"
b = 78
c = 89.213328

print("format %s" % a)
print("format %d" % b)
print("format %f" % c)

print("format %06d" % b)
print("format %.02f" % c)

print("format %s %d %f" % (a, b, c))


print("format %0.2f%%" % c)
