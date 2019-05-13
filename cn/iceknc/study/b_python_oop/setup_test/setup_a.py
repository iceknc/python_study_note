class Animal:
    def sleep(self):
        print("sleep")


class Cat(Animal):
    def __init__(self, name):
        print("初始化Cat %s" % name)
        self.__name = name

    def __eat(self):
        print("Cat eat %s" % self.__name)

    def sleep(self):
        super().sleep()
        print("Cat sleep")

    @classmethod
    def fuck(cls):
        pass

    @staticmethod
    def run():
        pass


if __name__ == "__main__":
    cat = Cat("Tom")
    print(cat._Cat__name)
    cat._Cat__eat()
    cat.sleep()
