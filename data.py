import os
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1', user='root',passwd='1234567890')
conn.select_db('data')
cursor = conn.cursor()

altnat_explode = ['|',',']

dir1 = '/home/wangyang/data/7k7k/2000-1/'
dir2 = '/home/wangyang/data/17173_6208/'
dir3 = '/home/wangyang/data/178/'

mysql_insert = "insert into `%s` (account,password) values (%s,%s)"
mysql_insert_17173 = "insert into `%s` (account,password,email,clearpassword) values (%s,%s,%s,%s)"

def read_to_mysql(dir,sql,table,start,end):
    i =0;

    cursor.execute("truncate table %s",table)
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
                cursor.execute(sql,params)
            except KeyboardInterrupt:
                break
            except :
                pass
            else:
                pass
            finally:
                pass

            line = file.readline()

# read_to_mysql(dir1,'\t','7k7k',0,2)

read_to_mysql(dir2,mysql_insert_17173,'17173',0,4)

read_to_mysql(dir3,mysql_insert,'178',1,3)