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
dir2 = datadir+'17173_6208/'
dir3 = datadir+'178/'

def combine_files():
    

def read_to_mysql(dir,sql,table,start,end):
    i =0;

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
            if len(list ) < 2:
                print list
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

read_to_mysql(dir2,mysql_insert_17173,'17173',0,4)

#read_to_mysql(dir3,mysql_insert_178,'178',1,3)