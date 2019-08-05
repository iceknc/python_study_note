# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/5
# @Desc  : 
"""
数据查询
    find() 查询
        db.集合名称.find({条件文档})
    findOne() 查询，只返回第一个
        db.集合名称.findOne({条件文档})
    pretty() 将结果格式化
        db.集合名称.find({条件文档}).pretty()

比较运算符
    等于:     默认是等于判断，没有运算符
    小于:     $lt (less than)
    小于等于:  $lte (less than equal)
    大于:     $gt (greater than)
    大于等于:  $gte (greater than equal)
    不等于:    $ne (not equal)

        db.集合名称.find({age:{$get:18}})

逻辑运算符
    and: 在json中写多个条件即可
        查询年龄大于或等于18，并且性别为true的学生
            db.stu.find({age:{$gte:19}, gender:true})
    or: 使用$or  值为数组   数组中每个元素为json
        查询年龄大于18， 或者性别为false的学生
            db.stu.find({$or:[{age:{$gt:18}},{gender:false}]})
        查询年龄大于18或者性别为男生,并且姓名是郭靖
            db.stu.find({$or:[{age:{$gt:18}},{gender:true}], name:"gj"})

范围运算符
    in： 在某个范围内
        查询年龄为18、28的学生
            db.stu.find({age:{$in:[18,28]}})
    nin: 不在某个范围内

正则表达式
    使用//或$regex编写正则表达式
        查询姓黄的学生
            db.stu.find({name:/^黄/})
            db.stu.find({name:{$regex:"^黄"}})

limit和skip
    limit()   用于读取指定数量的文档
        查询两条学生信息
            db.stu.find().limit(2)

    skip()    用于跳过指定数量的文档
        可用作翻页
            db.stu.find().skip(5)

自定义查询
    使用$where后面写一个函数，返回满足条件的数据
        查询年龄大于30的学生
            db.stu.find({
                $where:function() {
                    return this.age>30;}
            })

投影
    在查询到的返回结果中，只选择必要的字段
        db.集合名称.find({},{字段名称:1, ...})
        值为1表示显示，值为0不显示，对于_id列默认是显示的，如果不显示需要明确设置为0
            db.stu.find({},{_id:0,name:1,gender:1})
        新版本好像除了_id  其他列都不能设为0, 设置为1就是显示，不设置就是不显示

排序
    sort()  用于对集合排序
        db.集合名称.find().sort({字段:1, ...})
        值1为升序排列 值-1为降序排列
            db.stu.find().sort({gender:1, age:-1})

统计个数
    count()  用于统计结果集中文档条数
        db.集合名称.find({条件}).count()
            db.stu.find({gender:true}).count()
        db.集合名称.count({条件})
            db.stu.count({age:{$gt:20},gender:true})

消除重复
    distinct() 对数据进行去重
        db.集合名称.distinct('去重字段',{条件})
            db.stu.distinct('hometown',{age:{$gt:18}})
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






