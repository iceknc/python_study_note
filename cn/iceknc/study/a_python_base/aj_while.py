"""
while
break
continue

赋值运算符
=    c=a+b
+=   c+=a   c=c+a
-=   c-=a   c=c-a
*=   c*=a   c=c*a
/=   c/=a   c=c/a
//=  c//=a  c=c//a
%=   c%=a   c=c%a
**=  c**=a  c=c**a


\t  制表符
\n  换行符
"""

count = 10

while count > 0:
    print("hello %d" % count)
    count = count - 1

count = 10
while True:
    print("python %d" % count)
    count = count - 1
    if count <= 0:
        break
    else:
        continue

i = 1
j = 1

#99乘法表
while i < 10:
    j = 1
    while j <= i:
        print("%d * %d = %d" % (j, i, i * j), end="\t")
        j += 1
    i += 1
    print("\n", end="")
