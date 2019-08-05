# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/8/5
# @Desc  : 
"""
聚合
    基于数据处理的聚合管道，每个文档通过一个由多个阶段组成的管道，可以对每个阶段的管道进行分组，过滤等功能
    然后经过一系列的处理，输出相应的结果

    db.集合名称.aggregate({管道:{表达式}})

    在mongodb中，文档处理完毕后，通过管道进行下一次处理

    常用管道如下：
        $group:    将集合中的文档分组，可用于统计结果
            _id表示分组的依据，使用某个字段的格式为 $字段
            对应的字典中有几个键，结果中就有几个键
            统计男生，女生的总人数
                db.stu.aggregate({
                    $group:{
                        _id:"$gender",  //_id:{xxx:"$xxx",yyy:"$yyy"} 多条件分组  后面的管道取值 _id.xxx  _id.yyy
                        counter:{$sum:1}
                    }
                })
            求学生总人数，平均年龄
                db.stu.aggregate({
                    $group:{
                        _id:null;
                        counter:{$sum:1},
                        avg_age:{$avg:{"$age"}}
                    }
                })

        $match:    过滤数据，只输出符合条件的文档
            match是管道命令，能将结果交给后一个管道，但是find不行
            查询年龄大于20的学生
                db.stu.aggregate({
                    $match:{
                        age:{$gt:20}
                    }
                })
            查询年龄大于20的男生，女生人数
                 db.stu.aggregate(
                    {$match:{age:{$gt:20}}},
                    {$group:{_id:"$gender", counter:{$sum:1}}}
                 )

        $project:  修改输入文档的结构，如重命名、增加、删除字段、创建计算结果
            查询学生的姓名、年龄
                db.stu.aggregate(
                    {$project:{_id:0,name:1,age:1}}
                )
            查询男生、女生人数，输出人数
                db.stu.aggregate(
                    {$group:{_id:"$gender", counter:{$sum:1}}},
                    {$project:{_id:0,gender:"$_id",counter:1}}
                )

        $sort:     将输入文档排序后处处
            查询学生信息，按年龄升序
                db.stu.aggregate(
                    {$sort:{age:1}}
                )
            查询男生、女生人数,按人数降序
                db.stu.aggregate(
                    {$group:{_id:"$gender", counter:{$sum:1}}},
                    {$sort:{counter:-1}}
                )
        $limit:    限制聚合管道返回的文档数
            查询2条学生信息
                db.stu.aggregate(
                    {$limit:2}
                )

        $skip:     跳过指定数量的文档，并返回余下的文档
            查询从第3条开始的学生信息
                db.stu.aggregate(
                    {$skip:2}
                )
            统计男生、女生人数，按人数升序排列，取第二条数据
                db.stu.aggregate(
                    {$group:{_id:"$gender", counter:{$sum:1}}},
                    {$sort:{counter:1}},
                    {$skip:1},
                    {$limit:1},    //注意顺序，先写skip，再写limit
                )

        $unwind:   将数组类型的字段进行拆分
            db.集合名称.aggregate({$unwind:"$字段名称"})
                db.t2.insert({_id:1,item:'t-shirt',size:['S','M','L']})
                db.t2.aggregate({$unwind:'$size'})
                    结果如下
                    { "_id" : 1, "item" : "t-shirt", "size" : "S" }
                    { "_id" : 1, "item" : "t-shirt", "size" : "M" }
                    { "_id" : 1, "item" : "t-shirt", "size" : "L" }
            属性preserveNullAndEmptyArrays值为true表示保留属性值为空的文档，默认为false
                db.t2.aggregate({
                    $unwind:{
                        path:"$字段",
                        preserveNullAndEmptyArrays:true
                    }
                })

    常用表达式：
        $sum：     计算总和， $sum:1 表示以一倍计数
        $avg：     计算平均值
        $min：     获取最小值
        $max：     获取最大值
        $push：    在结果文档中插入值到一个数组中
        $first：   根据资源文档的排序获取第一个文档数据
        $last：    根据资源文档的排序获取最后一个文档数据
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






