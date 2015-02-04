#! /usr/bin/python
#-*-coding:utf-8-*- 
import dbus
import os
import sys
import json
# 该接口为测试环境
SERVICE_NAME='com.mock.frontServer'
OBJECT_PATH='/com/mock/frontServer/object'
INTERFACE='com.mock.frontServerInterface'
# 该接口为生产环境
# SERVICE_NAME='com.bmjc.ui'
# OBJECT_PATH='/bmjc/ui'
# INTERFACE='bmjc.ui'
arguments=sys.argv
class Father:
    def __init__(self):
        pass
    def handleResultMsg(self,resultMsgToUIPara):
        temp=arguments[1]
        temp=json.loads(temp)
        temp1={}
        temp1["scenename"]=str(temp["scenename"])
        temp1["functionname"]=str(temp["functionname"])
        temp1["resulttype"]=""
        temp1["result"]=resultMsgToUIPara   
        return json.dumps(temp1)
    def sendMsgToUI(self, resultMsg):        
        print '.............'       
        print '子进程('+str(os.getpid())+")开始处理.."
        bus =dbus.SessionBus()
        obj = bus.get_object(SERVICE_NAME,OBJECT_PATH)
        iface =dbus.Interface(obj,INTERFACE) 
        resultMsgToUI=Father.handleResultMsg(self,resultMsg)        
        print "send to mockFrontServer:"+resultMsgToUI  
        responseMsgFromUI = iface.updateFromTool(resultMsgToUI)   
        print "receive from mockFrontServer:"+responseMsgFromUI        
        print '子进程('+str(os.getpid())+")处理结束.."  
    
         


 