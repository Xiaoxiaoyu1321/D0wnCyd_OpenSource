import requests
import sys
import os

version = "b0.1"
#print("get value",len(sys.argv)) #打印出收到的传入命令行
#print(sys.argv) #打印出命令行
Cydia_User_Agent = "Cydia/0.9 CFNetwork/711.5.6 Darwin/14.0.0" #设置Cydia User-Agent



def GetCydiaRepoPackages(repo,get_way):
    print('[Messages]GetCydiaRepoPackages Loaded')
    #请求头
    headers = {
        "User-Agent":Cydia_User_Agent
    }
    print('[Messages]User-Agent:',Cydia_User_Agent)
    requests.session()
    requests.keep_alive = False
    print('[Messages]Downloading....')
    response = requests.get(repo+"/Packages.gz",headers=headers) #获取Packages gz文件
    
    
    f = open("./Packages."+get_way,'a')
    f.write("")
    f.close()
    print('[Messages]Writing....')
    fd = os.open('./Packages.'+get_way,1)
    os.write(fd,response.content)
    os.close(fd)
    print('[Messages]Done')
    #os.mkdir('./Packages')
    #print(response.content.decode('utf-8'))

    
    



if sys.argv[1] == "get_packages" and len(sys.argv ) >= 4:
    GetCydiaRepoPackages(sys.argv[2],sys.argv[3])
else:
    print('MDydia_OpenSource Version ' + version)
    print('常用指令：')
    print('get_packages [源地址] [获取方式]' + '\n' + '获取方式：意为得到Packages 压缩文件的方式，如gz,bz2')