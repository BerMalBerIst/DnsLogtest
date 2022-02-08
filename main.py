# coding=utf-8
import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    a = name
    getDN = requests.get("http://www.dnslog.cn/getdomain.php?t=0.737729294552574")
    cookie = (requests.utils.dict_from_cookiejar(getDN.cookies))
    headers = {'Cookie': 'PHPSESSID=%s' % cookie['PHPSESSID']}
    print(headers)
    Domain = getDN.text
    print('域名是：%s' % Domain)
    # ret = subprocess.call("curl http://%s" % Domain) #此处加入poc
    getDN2 = requests.get("http://www.dnslog.cn/getrecords.php?t=0.23106326273308764", headers=headers)
    aaa = len(getDN2.text)
    if aaa > 2:
        print("出网")

    else:
        print("不出网")


if __name__ == '__main__':
    slogon = '''


  __________                _____         .__ __________             .___          __   
  \______   \ ___________  /     \ _____  |  |\______   \ ___________|   | _______/  |_ 
   |    |  _// __ \_  __ \/  \ /  \\__  \ |  | |    |  _// __ \_  __ \   |/  ___/\   __\\
   |    |   \  ___/|  | \/    Y    \/ __ \|  |_|    |   \  ___/|  | \/   |\___ \  |  |  
   |______  /\___  >__|  \____|__  (____  /____/______  /\___  >__|  |___/____  > |__|  
          \/     \/              \/     \/            \/     \/               \/        


    '''
    print(slogon)
    print_hi('PyCharm')





