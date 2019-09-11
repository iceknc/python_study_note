# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/27
# @Desc  :
import sqlite3
from pymysql import *

total = 0

def main():
    sqlite = sqlite3.connect('data.sqlite')
    mysql = connect(host='localhost', port=3306, user='root', password='iceknc', database='python_study',
                    charset='utf8')
    sqlite_cursor = sqlite.cursor()
    mysql_cursor = mysql.cursor()
    sqlite_cursor.execute('select * from province')
    province_list = sqlite_cursor.fetchall()

    code_list = []
    sql = 'insert into china_region(code, name) values '
    for pro in province_list:
        sql += "('%s','%s'), " % (pro[0], pro[1])
        code_list.append(pro[0])
    count = mysql_cursor.execute(sql[0:-2])
    global total
    total += count
    if count > 0:
        print("省级添加成功: %d  total:%d" % (count, total))
    mysql.commit()

    for pro_code in code_list:
        handle_province(pro_code, sqlite_cursor, mysql_cursor, mysql)

    sqlite.close()
    mysql.close()


def handle_province(pro_code, sqlite_cursor, mysql_cursor, mysql):
    sqlite_cursor.execute('select * from city where provinceCode=%s' % (pro_code,))
    city_list = sqlite_cursor.fetchall()

    mysql_cursor.execute('select * from china_region where code=%s' % (pro_code,))
    parent = mysql_cursor.fetchone()

    code_list = []
    sql = 'insert into china_region(code, name, parentCode, parentId) values '
    for city in city_list:
        sql += "('%s', '%s', '%s', '%s'), " % (city[0], city[1], pro_code, parent[0])
        code_list.append(city[0])
    count = mysql_cursor.execute(sql[0:-2])
    mysql.commit()
    global total
    total += len(city_list)
    total += count
    if count > 0:
        print("%s --> 市级添加成功: %d  total:%d" % (parent[2], count, total))

    for city_code in code_list:
        handle_city(parent[2], city_code, sqlite_cursor, mysql_cursor, mysql)


def handle_city(pro_name, city_code, sqlite_cursor, mysql_cursor, mysql):
    sqlite_cursor.execute('select * from area where cityCode=%s' % (city_code,))
    county_list = sqlite_cursor.fetchall()

    mysql_cursor.execute('select * from china_region where code=%s' % (city_code,))
    parent = mysql_cursor.fetchone()

    code_list = []
    sql = 'insert into china_region(code, name, parentCode, parentId) values '
    for county in county_list:
        sql += "('%s', '%s', '%s', '%s'), " % (county[0], county[1], city_code, parent[0])
        code_list.append(county[0])
    count = mysql_cursor.execute(sql[0:-2])
    mysql.commit()
    global total
    total += count
    if count > 0:
        print("%s -- %s ----> 县级添加成功: %d  total:%d" % (pro_name, parent[2], count, total))

    for county_code in code_list:
        handle_county(pro_name, parent[2], county_code, sqlite_cursor, mysql_cursor, mysql)


def handle_county(pro_name, city_name, county_code, sqlite_cursor, mysql_cursor, mysql):
    sqlite_cursor.execute('select * from street where areaCode=%s' % (county_code,))
    street_list = sqlite_cursor.fetchall()

    mysql_cursor.execute('select * from china_region where code=%s' % (county_code,))
    parent = mysql_cursor.fetchone()

    code_list = []
    sql = 'insert into china_region(code, name, parentCode, parentId) values '
    for street in street_list:
        sql += "('%s', '%s', '%s', '%s'), " % (street[0], street[1], county_code, parent[0])
        code_list.append(street[0])
    count = mysql_cursor.execute(sql[0:-2])
    mysql.commit()
    global total
    total += count
    if count > 0:
        print("%s -- %s -- %s ----> 乡级添加成功: %d  total:%d" % (pro_name, city_name, parent[2], count, total))

    for street_code in code_list:
        handle_street(pro_name, city_name, parent[2], street_code, sqlite_cursor, mysql_cursor, mysql)


def handle_street(pro_name, city_name, county_name, street_code, sqlite_cursor, mysql_cursor, mysql):
    sqlite_cursor.execute('select * from village where streetCode=%s' % (street_code,))
    village_list = sqlite_cursor.fetchall()

    mysql_cursor.execute('select * from china_region where code=%s' % (street_code,))
    parent = mysql_cursor.fetchone()

    sql = 'insert into china_region(code, name, parentCode, parentId) values '
    for village in village_list:
        sql += "('%s', '%s', '%s', '%s'), " % (village[0], village[1], street_code, parent[0])
    count = mysql_cursor.execute(sql[0:-2])
    mysql.commit()
    global total
    total += count
    if count > 0:
        print("%s -- %s -- %s -- %s ----> 村级添加成功: %d  total:%d" % (
            pro_name, city_name, county_name, parent[2], count, total))


if __name__ == "__main__":
    main()
