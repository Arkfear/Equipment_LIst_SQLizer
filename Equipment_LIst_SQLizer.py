#encoding = utf-8
import os
import sys
import base64

VAS = "4"
CQM = "5"
MOFA = "6"
TMS = "7"
Other = "8"

openfile = open('egroup').readlines()
count = 0
for line in openfile:
    count +=1
    line = line.replace("\n","")
    ip,name,group = line.split()
    name = base64.b64encode(name.encode("ascii"))
    name = name.decode("utf-8")

    if group == "VAS":
        avg=(VAS,name,ip)
    elif group == "CQM":
        avg=(CQM,name,ip)
    elif group == "MOFA":
        avg=(MOFA,name,ip)
    elif group == "TMS":
        avg=(TMS,name,ip)
    else: 
        avg=(Other,name,ip)

    formate = "(%s,\"%s\",\"%s\",\"syslog\",\"utf-8\",\"zh_tw\"),"
    print(formate % avg)
