import wx
import socket
import _thread
import time
from bs4 import BeautifulSoup
import requests
import easygui


version = "1.0 Open"
class Main_Windows():
    
    def Main_Window():
        app = wx.App()
        titleq = "MDydia 开源版本 V" + version
        frame = wx.Frame(None,title=titleq,pos=(200,200),size=(600,400))
        #####
        global CydiaRepoAdd
        CydiaRepoAdd = wx.TextCtrl(frame,pos=(5,5),size = (200,30))
        CydiaRepoAdd.SetValue('apt.xiaoyustudio.com')
        
        CydiaRepoOK_Button = wx.Button(frame,label="Load",pos=(205,5),size=(50,30))
        #####
        frame.Show()
        app.MainLoop()
    

def ErrorMessage(Msg,Mod):
    ErrorVersion ="当前版本 V " + version
    ErrorMsg = "错误信息：" +  Msg
    ErrorMod = "错误模块:"+Mod
    easygui.msgbox('当前程序遇到错误\n' + ErrorVersion +"\n" + ErrorMsg + "\n" + ErrorMod)


Main_Windows.Main_Window()

