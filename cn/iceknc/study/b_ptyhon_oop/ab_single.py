"""
单例设计模式
    让类创建的对象，在系统中只有唯一的一个对象
    每一次执行 类名() 返回的对象，内存地址都是相同的

    __new__(cls)方法
        在内存中为对象分配空间
        返回对象的引用

    重写时一定要 return super().__new__(cls)
    __new__(cls) 是一个静态方法，在调用时需要主动传递 cls 参数
"""


class Player(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        print("__new__")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if Player.init_flag:
            return
        print("__init__")
        Player.init_flag = True


player = Player()
