import os
import mysql.connector
import traceback
conn = mysql.connector.connect(user='root', password='1234567890',
                              host='127.0.0.1',
                              database='data')
cursor = conn.cursor()

altnat_explode = ['|',',']
datadir = "/home/wangyang/data/"

dir1 = datadir+'7k7k/2000-1/'
dir2 = datadir+'17173/'
dir3 = datadir+'178/'
dir4 = datadir+'tianya/'
dir5 = datadir+'duduniu/'
dir6 = datadir+'taipingyang/'
dir7 = datadir+'weibo/'
dir8 = datadir+'renren/'
dir9 = datadir+'aipai/'
dir10 = datadir+'mop/'


mysql_create_7k7k = """CREATE TABLE IF NOT EXISTS `7k7k`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50),
                    `password` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""
mysql_create_178 = """CREATE TABLE IF NOT EXISTS `178`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50),
                    `password` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""
mysql_create_17173 = """CREATE TABLE IF NOT EXISTS `17173`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50),
                    `password` VARCHAR(50),
                    `email` VARCHAR(50),
                    `password_md5` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""
mysql_create_tianya = """CREATE TABLE IF NOT EXISTS `tianya`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50),
                    `password` VARCHAR(50),
                    `email` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""
mysql_create_duduniu = """CREATE TABLE IF NOT EXISTS `duduniu`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50),
                    `password` VARCHAR(50),
                    `email` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""

mysql_create_taipingyang = """CREATE TABLE IF NOT EXISTS `taipingyang`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50),
                    `password` VARCHAR(50),
                    `email` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""
mysql_create_weibo = """CREATE TABLE IF NOT EXISTS `weibo`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50) unique,
                    `password` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""
mysql_create_renren = """CREATE TABLE IF NOT EXISTS `renren`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50) unique,
                    `password` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""
mysql_create_aipai = """CREATE TABLE IF NOT EXISTS `renren`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50) unique,
                    `password` VARCHAR(50),
                    `email` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""
mysql_create_mop = """CREATE TABLE IF NOT EXISTS `renren`(  
                    `id` INT(10) NOT NULL AUTO_INCREMENT,
                    `account` VARCHAR(50) unique,
                    `password` VARCHAR(50),
                    PRIMARY KEY (`id`)
                    );"""

cursor.execute(mysql_create_17173)
cursor.execute(mysql_create_7k7k)
cursor.execute(mysql_create_178)
cursor.execute(mysql_create_tianya)
cursor.execute(mysql_create_duduniu)
cursor.execute(mysql_create_taipingyang)
cursor.execute(mysql_create_weibo)
cursor.execute(mysql_create_renren)
cursor.execute(mysql_create_aipai)
cursor.execute(mysql_create_mop)
mysql_insert_7k7k = "insert into `7k7k` (account,password) values (%s,%s)"
mysql_insert_178 = "insert into `178` (account,password) values (%s,%s)"
mysql_insert_17173 = "insert into `17173` (account,password_md5,email,password) values (%s,%s,%s,%s)"
mysql_insert_tianya = "insert into `tianya` (account,password,email) values (%s,%s,%s)"
mysql_insert_duduniu = "insert into `duduniu` (account,password,email) values (%s,%s,%s)"
mysql_insert_taipingyang = "insert into `taipingyang` (account,password,email) values (%s,%s,%s)"
mysql_insert_weibo = "insert into `weibo` (account,password) values (%s,%s)"
mysql_insert_renren = "insert into `renren` (account,password) values (%s,%s)"
mysql_insert_aipai = "insert into `aipai` (account,password,email) values (%s,%s)"
mysql_insert_mop = "insert into `mop` (account,password) values (%s,%s)"


def read_to_mysql(dir,sql,table,start,end):
    i =0;
    paramnum = end - start
    cursor.execute("TRUNCATE `%s` " %(table))
    for filename in os.listdir(dir):
        print filename
        filepath = dir+filename
        file = open(filepath)
        line = file.readline()

        # find explode
        explode = ''
        for exp in altnat_explode:
            if line.find(exp) >= 0:
                explode = exp

        while len(line) > 0 :
            line = line.rstrip('\r\n')
            line = line.replace('\n','')
            line = line.replace('\r','')
            if explode == '':
                list = line.split()
            else:
                list = line.split(explode)
            list = list[start:end]
            param = []
            for l in list:
                param.append(l.replace('\t',''))
            if len(list ) < paramnum:
                print list
            if len(list) == paramnum - 1:
                param.append('');
            if i % 10000 == 0 :
                print i
            i+=1
            try:
                cursor.execute(sql,param)
            except KeyboardInterrupt:
                break
            except Exception,e:
                print e
                print traceback.format_exc()
            else:
                pass
            finally:
                pass

            line = file.readline()

# read_to_mysql(dir1,mysql_insert_7k7k,'7k7k',0,2)

#read_to_mysql(dir2,mysql_insert_17173,'17173',0,4)

#read_to_mysql(dir3,mysql_insert_178,'178',1,3)

#read_to_mysql(dir4,mysql_insert_tianya,'tianya',0,3)

# read_to_mysql(dir5,mysql_insert_duduniu,'duduniu',0,3)

# read_to_mysql(dir6,mysql_insert_taipingyang,'taipingyang',0,3)

# read_to_mysql(dir7,mysql_insert_weibo,'weibo',0,3)

# read_to_mysql(dir8,mysql_insert_renren,'renren',0,3)

read_to_mysql(dir9,mysql_insert_aipai,'aipai',0,3)

read_to_mysql(dir10,mysql_insert_mop,'mop',0,2)
