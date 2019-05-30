# -*- coding: utf-8 -*-
# @Author: 徐志鹏
# @Date  : 2019/5/30
# @Desc  : 
"""
 配置主从同步的基本步骤
    在主服务器上，必须开启二进制日志机制和配置一个独立的ID
    在每一个从服务器上，配置一个唯一的ID，创建一个用来专门复制主服务器数据的账号
    在开始复制进程前，在主服务器上记录二进制文件的位置信息
    如果在开始复制之前，数据库中已经有数据，就必须先创建一个数据快照（可以使用mysqldump导出数据库，或者直接复制数据文件）
    配置从服务器要连接的主服务器的IP地址和登陆授权，二进制日志文件名和位置

    备份主服务器原有数据到从服务器
        如果在设置主从同步前，主服务器上已有大量数据，可以使用mysqldump进行数据备份并还原到从服务器以实现数据的复制。
        mysqldump -uroot -pmysql --all-databases --lock-all-tables > ~/master_db.sql
    在从服务器Windows上进行数据还原
        mysql –uroot –pxxxx < master_db.sql
    配置主服务器master
        编辑设置mysqld的配置文件，设置log_bin和server-id
            log_bin=/var/log/mysql/mysql-bin.log
            server-id=1
        重启mysql服务
            sudo service mysql restart
        登入主服务器的mysql，创建用于从服务器同步数据使用的帐号
            mysql –uroot –pmysql
            GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%' identified by 'slave';
            FLUSH PRIVILEGES;
        获取主服务器的二进制日志信息
            SHOW MASTER STATUS;
    配置从服务器slave
        找到MySQL的配置文件,设置server-id
            server-id=1
        重启mysql服务
            sudo service mysql restart
        进入mysql,设置连接到master主服务器
            change master to master_host='xxx.xxx.xxx.xxx', master_user='slave', master_password='slave',
            master_log_file='mysql-bin.000006', master_log_pos=590;
        开启同步，查看同步状态
            start slave;
            show slave status \g;
"""

def main():
    pass


if __name__ == "__main__":
    main()
    






