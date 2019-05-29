# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/29
# @Desc  : 

from pymysql import *


def main():
    # 创建Connection连接
    conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='iceknc', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()

    # 查询
    count = cs.execute("select * from goods")
    # 打印受影响的行数
    print("查询到%d条数据:" % count)
    for i in range(int(count / 2)):
        # 获取查询的结果
        result = cs.fetchone()
        # 打印查询的结果
        print(result)
        # 获取查询的结果

    #上面遍历剩下的一次性输出
    result = cs.fetchall()
    print(result)

    # 执行insert语句，并返回受影响的行数：添加一条数据
    # 增加
    # count = cs.execute('insert into goods_cates(name) values("硬盘")')
    # # 更新
    # count = cs1.execute('update goods_cates set name="机械硬盘" where name="硬盘"')
    # # 删除
    # count = cs1.execute('delete from goods_cates where id=6')

    # 提交之前的操作，如果之前已经之执行过多次的execute，那么就都进行提交
    conn.commit()

    # 关闭Cursor对象
    cs.close()
    # 关闭Connection对象
    conn.close()


if __name__ == "__main__":
    main()
