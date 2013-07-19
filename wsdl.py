import SOAPpy
import os
remoteurl = 'http://192.168.112.122:8080/XACML_Project_Server/webService/publish?wsdl'
name_space = 'http://service.xp.iie.cas.org/'
server = SOAPpy.SOAPProxy(remoteurl,namespace = name_space)
print server.sayHi(arg0 = 'ass')
os.system("pause")
