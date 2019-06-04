# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/30
# @Desc  : 
import re
import pymysql

template_root = "./templates"

# ----------更新----------
# 用来存放url路由映射
# url_route = {
#   "/index.py": index_func,
#   "/center.py": center_func
# }
g_url_route = dict()


def route(url):
    def func1(fun):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url] = fun

        def func2(file_name):
            return fun(file_name)

    return func1


@route("/index_advance.html")
def index(file_name):
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name, encoding="utf-8")
    except Exception as  ret:
        return "%s" % str(ret)
    else:
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
                            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                        </td>
                        </tr>"""

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[1])
        content = re.sub("\{%content%\}", html, content)
        return content


@route("/center_advance.html")
def center(file_name):
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name, encoding="utf-8")
    except Exception as  ret:
        return "%s" % str(ret)
    else:
        content = f.read()
        f.close()

        conn = pymysql.connect(host='localhost', port=3306, user='root', password='iceknc', database='stock_db',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,j.note_info from info as i inner join focus as j on i.id=j.info_id;")
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
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                </td>
            </tr>
            """

        html = ""

        for info in data_from_mysql:
            html += html_template % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[0], info[0])
        content = re.sub("\{%content%\}", html, content)
        return content

        return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    try:
        return g_url_route[file_name](file_name)
    except Exception as ret:
        return "%s" % str(ret)
