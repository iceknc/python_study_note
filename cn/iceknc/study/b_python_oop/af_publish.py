"""
制作发布压缩包步骤
    1.创建 setup.py
        from distutils.core import setup
        setup(name="包名",
               version="版本",
               description="描述信息",
               long_description="完整的描述信息",
               author="作者",
               author_email="作者邮箱",
               url="主页",
               py_module=["xxx", "yyy"])
    2.构建模块
        python3 setup.py build
    3.生成发布压缩包
        python3 setup.py sdist

安装模块
    windows
        下载压缩包
        解压
        进入解压目录 python setup.py install
    ubuntu
        tar -zxvf xxx.tar.gz
        进入解压目录 sudo python3 setup.py install

删除模块
    
"""