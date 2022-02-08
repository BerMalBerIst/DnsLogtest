# coding=utf-8
# This is a sample Python script.
import requests
import re
from time import time
import sys
import subprocess
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    a=name
    getDN = requests.get("http://www.dnslog.cn/getdomain.php?t=0.737729294552574")
    cookie = (requests.utils.dict_from_cookiejar(getDN.cookies))
    headers = {'Cookie' : 'PHPSESSID=%s'%cookie['PHPSESSID']}
    print (headers)
    Domain=getDN.text
    print('域名是：%s'%Domain)
    #ret = subprocess.call("curl http://%s" % Domain) #此处加入poc
    getDN2 = requests.get("http://www.dnslog.cn/getrecords.php?t=0.23106326273308764",headers=headers)
    aaa = len(getDN2.text)
    if aaa>2:
        print("出网")
    else:
        print("不出网")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
