# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/30
# @Desc  : 
import re
import pymysql
import logging

template_root = "./templates"

# ----------更新----------
# 用来存放url路由映射
# url_route = {
#   "/index.py": index_func,
#   "/center.py": center_func
# }
g_url_route = dict()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT["/index.py"] = index
        g_url_route[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return set_func


@route(r"/index_ultimate.html")
def index(ret):
    with open("./templates/index_ultimate.html", encoding="utf-8") as f:
        content = f.read()
        f.close()

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='iceknc', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from info;")
    data_from_mysql = cursor.fetchall()
    cursor.close()
    conn.close()

    html_template = """
        <tr>
            <td>%d</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemIdValue="%s">
            </td>
        </tr>"""

    html = ""

    for info in data_from_mysql:
        html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])
    content = re.sub("\{%content%\}", html, content)
    return content


@route(r"/center_ultimate.html")
def center(ret):
    with open("./templates/center_ultimate.html", encoding="utf-8") as f:
        content = f.read()
        f.close()

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='iceknc', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute(
        "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,j.note_info from info as i inner join focus as j on i.id=j.info_id;")
    data_from_mysql = cursor.fetchall()
    cursor.close()
    conn.close()

    html_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemIdValue="%s">
                </td>
            </tr>
            """

    html = ""

    for info in data_from_mysql:
        html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])
    content = re.sub("\{%content%\}", html, content)
    return content


@route(r"/add/(\d+)\.html")
def add_focus(ret):
    # 1 获取股票代码
    stock_code = ret.group(1)

    # 2 判断是否有这个股票代码
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='iceknc', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from info where code=%s;", (stock_code,))
    # 如果要是没有这个股票代码，那么久认为是非法
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "没有这支股票，大哥 ，我们是创业公司，请手下留情..."

    # 3 判断一下是否已经关注过
    cursor.execute("select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;", (stock_code))
    # 如果查出来了，那么表示已经关注过
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return "已经关注过了，请勿重复关注..."

    # 4 添加关注
    cursor.execute()
    cursor.execute("insert into focus (info_id) select id from info where code=%s;", (stock_code,))
    conn.commit()
    cursor.close()
    conn.close()

    return "关注成功"


@route(r"/del/(\d+)\.html")
def del_focus(ret):
    # 1 获取股票代码
    stock_code = ret.group(1)

    # 2 判断是否有这个股票代码
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='iceknc', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from info where code=%s;", (stock_code,))

    # 如果要是没有这个股票代码，那么久认为是非法
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "没有这支股票，大哥 ，我们是创业公司，请手下留情..."

    # 3 判断一下是否已经关注过
    cursor.execute("select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;", (stock_code,))
    # 如果查出来了，那么表示已经关注过
    if not cursor.fetchone():
        cursor.close()
        conn.close()
        return "%s 之前未关注，请勿取消关注..." % stock_code

    # 4. 取消关注
    cursor.execute("delete from focus where info_id = (select id from info where code=%s);", (stock_code,))
    conn.commit()
    cursor.close()
    conn.close()

    return "取消关注成功...."


@route(r"/update/(\d+)\.html")
def show_update_page(ret):
    """显示修改的那个页面"""
    # 1. 获取股票代码
    stock_code = ret.group(1)

    # 2. 打开模板
    with open("./templates/update.html",encoding="utf-8") as f:
        content = f.read()

    # 3. 根据股票代码查询相关的备注信息
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='iceknc', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select f.note_info from focus as f inner join info as i on i.id=f.info_id where i.code=%s;",
                   (stock_code,))
    stock_infos = cursor.fetchone()
    note_info = stock_infos[0]  # 获取这个股票对应的备注信息
    cursor.close()
    conn.close()

    content = re.sub(r"\{%note_info%\}", note_info, content)
    content = re.sub(r"\{%code%\}", stock_code, content)

    return content


@route(r"/update/(\d+)/(.*)\.html")
def save_update_page(ret):
    """"保存修改的信息"""
    stock_code = ret.group(1)
    comment = ret.group(2)

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='mysql', database='stock_db',
                           charset='utf8')
    cursor = conn.cursor()
    cursor.execute("update focus set note_info=%s where info_id = (select id from info where code=%s);",
                   (comment, stock_code))
    conn.commit()
    cursor.close()
    conn.close()

    return "修改成功..."


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    logging.basicConfig(level=logging.INFO,
                        filename='./log.txt',
                        filemode='a',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    logging.info("访问的是，%s" % file_name)

    try:
        for url, func in g_url_route.items():
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else:
            return "请求的url(%s)没有对应的函数...." % file_name
    except Exception as ret:
        return "%s" % str(ret)
