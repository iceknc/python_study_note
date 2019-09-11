# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/27
# @Desc  :
import sqlite3
from pymysql import *
import multiprocessing
import os


def main():
    sqlite = sqlite3.connect('data.sqlite')
    sqlite_cursor = sqlite.cursor()
    sqlite_cursor.execute('select * from province')
    province_list = sqlite_cursor.fetchall()
    p_list = {p[0]: p[1] for p in province_list}
    sqlite_cursor.close()

    pool = multiprocessing.Pool(8)
    for code in p_list:
        if code != '11':
            continue
        pool.apply_async(from_province, (code, p_list[code]))
    pool.close()
    pool.join()


def write():
    file_list = []
    for main_dir, sub_dir, sub_file in os.walk("F:\\pro"):
        for name in sub_file:
            file_list.append(os.path.join("F:\\pro", name))

    mysql = connect(host='localhost', port=3306, user='root', password='iceknc', database='python_study',
                    charset='utf8')
    cursor = mysql.cursor()
    count = 0
    for file in file_list:
        with open(file, "r", encoding='utf-8') as f:
            sql = f.readline()
            while sql:
                cursor.execute(sql)
                count += 1
                if count % 10 == 0:
                    mysql.commit()
                    print("commit:%d" % (count,))
                sql = f.readline()
            else:
                print(f.name + "  -----------> finish")
        mysql.commit()


def write_sql(p_code, p_name, sql):
    with open("F:\\pro\\sql_%s_%s" % (p_code, p_name), "a+", encoding='utf8') as f:
        print(sql)
        f.write(sql + "\n")


def from_province(p_code, p_name):
    sqlite = sqlite3.connect('data.sqlite')
    sqlite_cursor = sqlite.cursor()
    sqlite_cursor.execute("select * from province where code='%s'" % (p_code,))
    pro = sqlite_cursor.fetchone()
    sql = "insert into china_region(code, name) values ('%s','%s')" % (pro[0], pro[1])
    write_sql(p_code, p_name, sql)

    handle_province(pro, sqlite_cursor)

    sqlite.close()


def handle_province(pro, sqlite_cursor):
    sqlite_cursor.execute('select * from city where provinceCode=%s' % (pro[0]))
    city_list = sqlite_cursor.fetchall()

    sql = 'insert into china_region(code, name, provinceCode, parentCode) values '
    for city in city_list:
        sql += "('%s', '%s', '%s', '%s'), " % (city[0], city[1], city[2], pro[0])
    write_sql(pro[0], pro[1], sql[0:-2])

    for city in city_list:
        handle_city(pro, city, sqlite_cursor)


def handle_city(pro, city, sqlite_cursor):
    sqlite_cursor.execute('select * from area where cityCode=%s' % (city[0]))
    area_list = sqlite_cursor.fetchall()

    sql = "insert into china_region(code, name, cityCode, provinceCode, parentCode) values "
    for area in area_list:
        sql += "('%s', '%s', '%s', '%s', '%s'), " % (area[0], area[1], area[2], area[3], city[0])
    write_sql(pro[0], pro[1], sql[0:-2])

    for area in area_list:
        handle_area(pro, city, area, sqlite_cursor)


def handle_area(pro, city, area, sqlite_cursor):
    sqlite_cursor.execute('select * from street where areaCode=%s' % (area[0]))
    street_list = sqlite_cursor.fetchall()

    sql = "insert into china_region(code, name, countyCode, provinceCode, cityCode, parentCode) values "
    for street in street_list:
        sql += "('%s', '%s', '%s', '%s', '%s', '%s'), " % (
            street[0], street[1], street[2], street[3], street[4], area[0])
    write_sql(pro[0], pro[1], sql[0:-2])

    for street in street_list:
        handle_street(pro, city, area, street, sqlite_cursor)


def handle_street(pro, city, area, street, sqlite_cursor):
    sqlite_cursor.execute('select * from village where streetCode=%s' % (street[0]))
    village_list = sqlite_cursor.fetchall()

    sql = "insert into china_region(code, name, streetCode, provinceCode, cityCode, countyCode, parentCode) values "
    for village in village_list:
        sql += "('%s', '%s', '%s', '%s', '%s', '%s', '%s'), " % (
            village[0], village[1], village[2], village[3], village[4], village[5], street[0])
    write_sql(pro[0], pro[1], sql[0:-2])


if __name__ == "__main__":
    # main()
    write()
