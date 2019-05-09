"""
try:
    code...
except 类型1:
    code...
except (类型2, 类型3):
    code...
except 类型4 as ee:
    code...


捕获未知错误
except Exception:
    pass
"""

try:
    num = int(input("请输入一个数字"))
    result = 10 / num
    print(result)

    if result > 3:
        raise Exception("我是来搞笑的")
except ValueError:
    pass
except ZeroDivisionError as zde:
    pass
except Exception as e:
    pass
else:
    # 没有异常才会执行的代码
    pass
finally:
    # 有没有异常最终都会执行的代码
    pass
