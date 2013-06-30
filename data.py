import os
import MySQLdb

conn = MySQLdb.connect(host='192.168.1.100', user='root',passwd='asdfghjkl')
conn.select_db('data')
cursor = conn.cursor()

dir1 = 'D:\\database\\7k7k\\2000-1\\'

def read_to_mysql(dir,explode,table,start,end):
    i =0;
    cursor.execute("""CREATE TABLE IF NOT EXISTS `%s`(  
  `id` INT(10) NOT NULL AUTO_INCREMENT,
  `account` VARCHAR(50),
  `password` VARCHAR(50),
  PRIMARY KEY (`id`),
  UNIQUE INDEX (`account`)
    );""",table)
    cursor.execute("truncate table `%s`",table)
    for filename in os.listdir(dir1):
        filepath = dir1+filename
        file = open(filepath)
        line = file.readline()
        while len(line) > 0 :
            line = line.rstrip('\n')
            list = line.split(explode)
            print list

            line = file.readline()
            params = []
            params.append(table)
            params.extend(list)
            try:
                cursor.execute("insert into `%s` (account,password) values (%s,%s)",params)
            except KeyboardInterrupt:
                break
            except Exception, e:
                raise
            else:
                pass
            finally:
                pass


read_to_mysql(dir1,'\t','7k7k',0,1)


