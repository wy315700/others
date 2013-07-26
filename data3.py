import os
source = "D:\\source.txt"
dist   = "D:\\dist.txt"
out    = "D:\\out.txt"
        
source_file = open(source)
dist_file = open(dist)
out_file = open(out,"w")

dic = {};
line = dist_file.readline()

while len(line) > 0 :
    line = line.rstrip('\r\n')
    line = line.replace('\n','')
    line = line.replace('\r','')
            
    list = line.split(":")
    dic[list[0]] = list[1]
    line = dist_file.readline()

line = source_file.readline()
while len(line) > 0 :
    line = line.replace('\n','')
    line = line.replace('\r','')
    list = line.split("\t")
    if list[1] in dic:
        line = line + "\t" +  dic.get(list[1])
    line += "\n"
    out_file.writelines(line)
    line = source_file.readline()