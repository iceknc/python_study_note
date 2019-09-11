# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/9/4
# @Desc  : 
"""
CSRF
    CSRF全拼为Cross Site Request Forgery，译为跨站请求伪造。CSRF指攻击者盗用了你的身份，以你的名义发送恶意请求。
    CSRF能够做的事情包括：以你名义发送邮件，发消息，盗取你的账号，甚至于购买商品，虚拟货币转账......
    造成的问题包括：个人隐私泄露以及财产安全。
    如果想防止CSRF，首先是重要的信息传递都采用POST方式而不是GET方式
    在form表单中post提交时加入标签csrf_token
    当启用中间件并加入标签csrf_token后，会向客户端浏览器中写入一条Cookie信息，这条信息的值与隐藏域input元素的value属性是一致的，
    提交到服务器后会先由csrf中间件进行验证，如果对比失败则返回403页面，而不会进行后续的处理。

    示例 <use_mysql>/<test_app>.views.login
         <use_mysql>/<test_app>.views.login_check
         <use_mysql>/<test_app>.views.post
         <use_mysql>/<test_app>.views.post_action
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






