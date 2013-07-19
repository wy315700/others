import urllib2
import os
from HTMLParser import HTMLParser  
basrurl = "http://bbs.ngacn.cc/read.php?tid=6263940&page="

content = ""

class MyHTMLParser(HTMLParser):  
    def __init__(self):  
        HTMLParser.__init__(self)  
        self.flag = 0  
        self.links = []  
        self.title=""  
        
    def handle_starttag(self, tag, attrs):  
        #print "Encountered the beginning of a %s tag" % tag  
                              
        if tag =="span":
            if len(attrs) == 0: 
                pass  
            else:  
                for (variable, value)  in attrs:  
                    if variable == "class":  
                        if  value == "postcontent ubbcode":

                            self.flag=1  
        if tag == "br" and self.flag == 1:
            global content
            content += "\n"
          
    def handle_endtag(self,tag):
        if tag =="div":
            self.flag=0
    def handle_data(self,data):  
        if self.flag == 1:
            global content

            content += data  


file_object = open('D:\\thefile.txt', 'w')



for i in range(1,3):
    print i
    hp = MyHTMLParser()  
    req = urllib2.Request(basrurl + str(i));  
    response = urllib2.urlopen(req)
    data = response.read().decode("GBK")
    print data
    content = ""
    hp.feed(data)
    
    file_object.write(content.encode("GBK"))
    hp.close()  
file_object.close( )