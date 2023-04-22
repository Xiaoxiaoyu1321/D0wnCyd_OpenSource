import requests
import sys
import os
import configparser

version = "b0.1"
#print("get value",len(sys.argv)) #打印出收到的传入命令行
#print(sys.argv) #打印出命令行
Cydia_User_Agent = "Cydia/0.9 CFNetwork/711.5.6 Darwin/14.0.0" #设置Cydia User-Agent



def GetCydiaRepoPackages(repo,get_way): #下载Packages 文件
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
    
    
    #f = open("./Packages."+get_way,'a')
    #f.close()
    try:
        os.mkdir('./Packages')
        os.mkdir('./Downloads')
    except:
        pass

    path = r"./Packages/Packages."+get_way
    with open(path,'wb') as f:
        f.write(response.content)
   

    print('[Messages]Writing....')
    #fd = os.open(path,1)
    #os.write(fd,response.content)
    #os.close(fd)
    print('[Messages]Done')
    #os.mkdir('./Packages')
    #print(response.content.decode('utf-8'))
def LoadPackages(ways):
    if ways == "CRLF" or ways == 'crlf':
        file_a = '\r\n'
    elif ways == 'LF' or ways == 'lf':
        file_a = '\r'
    else:
        file_a = '\r\n'
    path = r"./Packages/Packages"
    print('[Messages]Files:' ,path)
    with open(path,'r',encoding='utf-8') as f:
        file_data = f.read()
        f.close()
    
    file_w = file_data.split(file_a)

    file_long = len(file_w)
    i = 0

    while i < file_long:
        #print(file_w[i])
        i = i +1

    #print(str(file_data))
    

    
def CommandHelp():
    print('MDydia_OpenSource Version ' + version)
    print('\n'+'常用指令：')
    print('get_packages [源地址] [获取方式]' + '\n' + '获取方式：意为得到Packages 压缩文件的方式，如gz,bz2')
    print('')
    print('packages load [换行符格式]'+'\n' + '换行符格式意为切换Windows 和 UNIX 系统下不同的换行符格式。' + '\n' + 'Windows 下换行符以 CRLF存在，UNIX(macOS)下以LF存在，若要调用此方法，请跟随CRLF 或 LF')



if len(sys.argv) >= 2:

    if sys.argv[1] == "get_packages" and len(sys.argv ) >= 4:
        GetCydiaRepoPackages(sys.argv[2],sys.argv[3])
    elif sys.argv[1] == 'packages' and len(sys.argv) >= 3:
        if sys.argv[2] == 'load' and len(sys.argv) >= 4:
            LoadPackages(sys.argv[3])

    else:
        CommandHelp()
    
else:
    CommandHelp()