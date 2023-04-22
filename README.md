# MDydia_OpenSource

#### 这是一个可以在线下载Cydia 源上的deb文件的软件
#### This is a software that can download deb files on Cydia source online.
### **关于这个软件**
##### 这是一个简单的Cydia 软件园爬取程序，现在的开源版本仍处在一个简易的命令行版本   
##### 起初创建这个软件就是为了方便用户下载Cydia 源的deb文件

### **如何使用**
#### 如果要开始使用这个软件，请先确保您的操作系统上安装了Python 3.6.x 或更新版本，这是必要的。如果您没有安装Python ，您可以去python.org 下载Python

#### 在安装好Python 以后，请使用pip 指令安装以下所需要的Python 包
```
requests
```
#### 当一切准备就绪以后，您便可以根据下面的指令来进行使用了。

### **下面列出了一些常用命令**

```
get_packages [源地址] [获取方式] 
```

### **下面是对一些常用命令的解释**
```
[源地址] 欲爬取的Cydia 源地址    
[获取方式] 许多Cydia 源采用gz 或 bz2 压缩包来储存及传输 Packages 文件，您可以在这里规定您是要使用bz2 压缩包还是要使用gz压缩包。请注意，不是所有源都提供有两种压缩包    
```
----
### **重要信息**
#### 此版本的更新较为缓慢，且只包括基础功能，现暂不实现高级功能，请见谅     
#### 若要使用更多功能以及更好的体验，请移步到 *原版MDydia*
----
### All Copyright 2019-2023 XiaoyuStudio
