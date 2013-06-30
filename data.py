import os
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root',passwd='1234567890')
conn.select_db('data')
cursor = conn.cursor()

dir1 = '/home/wangyang/data/7k7k/2000-1/'
dir2 = '/home/wangyang/data/17173_6208/'
dir3 = '/home/wangyang/data/178/'
def read_to_mysql(dir,explode,table,start,end):
    i =0;
    cursor.execute("""CREATE TABLE IF NOT EXISTS `%s`(  
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `account` VARCHAR(50),
  `password` VARCHAR(50),
  PRIMARY KEY (`id`)
    );""",table)
    cursor.execute("truncate table `%s`",table)
    for filename in os.listdir(dir):
        print filename
        filepath = dir+filename
        file = open(filepath)
        line = file.readline()
        while len(line) > 0 :
            line = line.rstrip('\n')
            list = line.split(explode)
            list = list[start:end]

            if i % 10000 == 0 :
                print i
            i+=1
            params = []
            params.append(table)
            params.extend(list)
            try:
                cursor.execute("insert into `%s` (account,password) values (%s,%s)",params)
            except KeyboardInterrupt:
                break
            except :
                pass
            else:
                pass
            finally:
                pass

            line = file.readline()

def read_to_mysql_17173(dir,explode,table,start,end):
    i =0;
    cursor.execute("""CREATE TABLE IF NOT EXISTS `%s`(  
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `account` VARCHAR(50),
  `password` VARCHAR(50),
  `email` VARCHAR(50),
  `clearpassword` VARCHAR(50),
  PRIMARY KEY (`id`)
    );""",table)
    cursor.execute("truncate table `%s`",table)
    for filename in os.listdir(dir):
        print filename
        filepath = dir+filename
        file = open(filepath)
        line = file.readline()
        while len(line) > 0 :
            line = line.rstrip('\n')
            list = line.split(explode)
            list = list[start:end]

            if i % 10000 == 0 :
                print i
            i+=1
            params = []
            params.append(table)
            params.extend(list)
            try:
                cursor.execute("insert into `%s` (account,password,email,clearpassword) values (%s,%s,%s,%s)",params)
            except KeyboardInterrupt:
                break
            except :
                pass
            else:
                pass
            finally:
                pass

            line = file.readline()

read_to_mysql(dir1,'\t','7k7k',0,2)

read_to_mysql_17173(dir2,'\t|\t','17173',0,4)

read_to_mysql(dir3,'\t','178',1,3)

