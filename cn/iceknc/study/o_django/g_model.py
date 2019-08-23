# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/23
# @Desc  : 
"""
定义属性
    Django根据属性的类型确定以下信息
        当前选择的数据库支持字段的类型
        渲染管理表单时使用的默认html控件
        在管理站点最低限度的验证

    django会为表创建自动增长的主键列，每个模型只能有一个主键列，如果使用选项设置某属性为主键列后django不会再创建自动增长的主键列
    默认创建的主键列属性为id，可以使用pk代替，pk全拼为primary key
        pk是主键的别名，若主键名为id2，那么pk是id2的别名

    属性命名限制
        不能是python的保留关键字
        不允许使用连续的下划线，这是由django的查询方式决定的
        定义属性时需要指定字段类型，通过字段类型的参数指定选项

字段类型
    使用时需要引入django.db.models包，字段类型如下
        AutoField: 自动增长的IntegerField，通常不用指定，不指定时Django会自动创建属性名为id的自动增长属性
        BooleanField: 布尔字段，值为True或False
        NullBooleanField: 支持Null、True、False三种值
        CharField(max_length=字符长度): 字符串
        TextField: 大文本字段，一般超过4000个字符时使用
        IntegerField: 整数
        DecimalField(max_digits=总位数, decimal_places=小数位数): 十进制浮点数，适用于跟钱相关的字段
        FloatField: 浮点数，精度不如DecimalField
        DateField(auto_now=False, auto_now_add=False): 日期
            auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳，它总是使用当前日期，默认为false。
            auto_now_add表示当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false。
            auto_now_add和auto_now是相互排斥的，组合将会发生错误
        TimeField: 时间，参数同DateField
        DateTimeField: 日期时间，参数同DateField
        FileField: 上传文件字段
        ImageField: 继承于FileField，对上传的内容进行校验，确保是有效的图片

选项
    通过选项实现对字段的约束，选项如下
        null: 如果为True，表示允许为空，默认值是False。
        blank: 如果为True，则该字段允许为空白，默认值是False。
            null是数据库范畴的概念，blank是表单验证范畴的。
        db_column: 字段的名称，如果未指定，则使用属性的名称。
        db_index: 若值为True, 则在表中会为此字段创建索引，默认值是False。
        default: 默认值。
        primary_key: 若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用。
        unique: 如果为True, 这个字段在表中必须有唯一值，默认值是False。

"""


def main():
    pass


if __name__ == "__main__":
    main()
