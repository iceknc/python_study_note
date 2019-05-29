# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/29
# @Desc  : 

from pymysql import *


def main():
    find_name = input("请输入物品名称：")

    # 创建Connection连接
    conn = connect(host='localhost', port=3306, user='root', password='iceknc', database='jing_dong', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()

    # # 非安全的方式
    # # 输入 " or 1=1 or "   (双引号也要输入)
    # sql = 'select * from goods where name="%s"' % find_name
    # print("""sql===>%s<====""" % sql)
    # # 执行select语句，并返回受影响的行数：查询所有数据
    # count = cs.execute(sql)

    # 安全的方式
    # 构造参数列表
    params = [find_name]
    # 执行select语句，并返回受影响的行数：查询所有数据
    count = cs.execute('select * from goods where name=%s', params)
    # 注意：
    # 如果要是有多个参数，需要进行参数化
    # 那么params = [数值1, 数值2....]，此时sql语句中有多个%s即可

    # 打印受影响的行数
    print(count)
    # 获取查询的结果
    # result = cs.fetchone()
    result = cs.fetchall()
    # 打印查询的结果
    print(result)
    # 关闭Cursor对象
    cs.close()
    # 关闭Connection对象
    conn.close()


if __name__ == "__main__":
    main()
