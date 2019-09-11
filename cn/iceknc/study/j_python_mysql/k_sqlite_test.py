# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/27
# @Desc  :
import sqlite3
from pymysql import *
import multiprocessing
import os
import time
from concurrent.futures import wait, ALL_COMPLETED, ProcessPoolExecutor


def main():
    executor = ProcessPoolExecutor(max_workers=2)
    all_task = [executor.submit(copy_data(49 - i)) for i in range(50)]
    wait(all_task, return_when=ALL_COMPLETED)
    print("finish " * 20)

    # pool = multiprocessing.Pool(4)
    # for i in range(50):
    #     pool.apply_async(copy_data, (49 - i,))
    #
    # pool.close()
    # while True:
    #     task = len(multiprocessing.active_children())
    #     print('----------------------------------------------------------------------------------------------------'
    #           '--------->>>> taskCount:%d' % (task,))
    #     time.sleep(10)
    #     if task == 0:
    #         break
    # pool.join()


def copy_data(index_num):
    print('----------------------------------------------------------------------------------------------------'
          '--------->>>> start work:%d' % (index_num,))
    sqlite = sqlite3.connect('data.sqlite')
    mysql = connect(host='localhost', port=3306, user='root', password='iceknc', database='python_study',
                    charset='utf8')
    sqlite_cursor = sqlite.cursor()
    mysql_cursor = mysql.cursor()
    sqlite_cursor.execute('select * from province')
    province_list = sqlite_cursor.fetchall()

    if index_num >= len(province_list):
        return
    pro = province_list[index_num]
    count = mysql_cursor.execute("insert into test_app_region(code, name) select '%s', '%s' from DUAL where not " \
                                 "exists(select * from test_app_region where code ='%s')" %
                                 (pro[0], pro[1], pro[0]))
    if count > 0:
        print("%d : %s --> 添加成功" % (os.getpid(), pro[1]))
    else:
        print("%d : %s --> 已经存在" % (os.getpid(), pro[1]))
    mysql.commit()
    handle_province(pro, sqlite_cursor, mysql_cursor, mysql)

    sqlite.close()
    mysql.close()


def handle_province(pro, sqlite_cursor, mysql_cursor, mysql):
    sqlite_cursor.execute('select * from city where provinceCode=%s' % (pro[0]))
    city_list = sqlite_cursor.fetchall()

    mysql_cursor.execute('select * from test_app_region where code=%s' % (pro[0]))
    parent = mysql_cursor.fetchone()

    for city in city_list:
        count = mysql_cursor.execute(
            "insert into test_app_region(code, name, provinceCode, parentCode, parent_id) select " \
            "'%s', '%s', '%s', '%s', '%s' from dual where not exists(select * from test_app_region " \
            "where code ='%s')" % (city[0], city[1], city[2], parent[1], parent[0], city[0]))

        if count > 0:
            print("%d : %s -- %s --> 添加成功" % (os.getpid(), pro[1], city[1]))
        else:
            print("%d : %s -- %s --> 已经存在" % (os.getpid(), pro[1], city[1]))
    mysql.commit()

    for city in city_list:
        handle_city(pro, city, sqlite_cursor, mysql_cursor, mysql)


def handle_city(pro, city, sqlite_cursor, mysql_cursor, mysql):
    sqlite_cursor.execute('select * from area where cityCode=%s' % (city[0]))
    area_list = sqlite_cursor.fetchall()

    mysql_cursor.execute('select * from test_app_region where code=%s' % (city[0]))
    parent = mysql_cursor.fetchone()

    for area in area_list:
        count = mysql_cursor.execute(
            "insert into test_app_region(code, name, provinceCode, cityCode, parentCode, parent_id) select " \
            "'%s', '%s', '%s', '%s', '%s', '%s' from dual where not exists(select * from test_app_region " \
            "where code ='%s')" % (area[0], area[1], area[2], area[3], parent[1], parent[0], area[0]))

        if count > 0:
            print("%d : %s -- %s -- %s --> 添加成功" % (os.getpid(), pro[1], city[1], area[1]))
        else:
            print("%d : %s -- %s -- %s --> 已经存在" % (os.getpid(), pro[1], city[1], area[1]))
    mysql.commit()

    for area in area_list:
        handle_area(pro, city, area, sqlite_cursor, mysql_cursor, mysql)


def handle_area(pro, city, area, sqlite_cursor, mysql_cursor, mysql):
    sqlite_cursor.execute('select * from street where areaCode=%s' % (area[0]))
    street_list = sqlite_cursor.fetchall()

    mysql_cursor.execute('select * from test_app_region where code=%s' % (area[0]))
    parent = mysql_cursor.fetchone()

    for street in street_list:
        count = mysql_cursor.execute(
            "insert into test_app_region(code, name, provinceCode, cityCode,countyCode, parentCode, parent_id) select " \
            "'%s', '%s', '%s', '%s', '%s', '%s', '%s' from dual where not exists(select * from test_app_region " \
            "where code ='%s')" % (
                street[0], street[1], street[2], street[3], street[4], parent[1], parent[0], street[0]))

        if count > 0:
            print("%d : %s -- %s -- %s -- %s --> 添加成功" % (
                os.getpid(), pro[1], city[1], area[1], street[1]))
        else:
            print("%d : %s -- %s -- %s -- %s --> 已经存在" % (
                os.getpid(), pro[1], city[1], area[1], street[1]))
    mysql.commit()

    for street in street_list:
        handle_street(pro, city, area, street, sqlite_cursor, mysql_cursor, mysql)


def handle_street(pro, city, area, street, sqlite_cursor, mysql_cursor, mysql):
    sqlite_cursor.execute('select * from village where streetCode=%s' % (street[0]))
    village_list = sqlite_cursor.fetchall()

    mysql_cursor.execute('select * from test_app_region where code=%s' % (street[0]))
    parent = mysql_cursor.fetchone()

    for village in village_list:
        count = mysql_cursor.execute(
            "insert into test_app_region(code, name,streetCode, provinceCode, cityCode,countyCode, " \
            "parentCode, parent_id) select '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' from dual " \
            "where not exists(select * from test_app_region where code ='%s')" % (
                village[0], village[1], village[2], village[3], village[4], village[5], parent[1], parent[0],
                village[0]))

        if count > 0:
            print("%d : %s -- %s -- %s -- %s -- %s --> 添加成功" % (
                os.getpid(), pro[1], city[1], area[1], street[1], village[1]))
        else:
            print("%d : %s -- %s -- %s -- %s -- %s --> 已经存在" % (
                os.getpid(), pro[1], city[1], area[1], street[1], village[1]))
    mysql.commit()


if __name__ == "__main__":
    main()
