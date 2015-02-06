#! /usr/bin/python
#-*-coding:utf-8-*- 
import dbus
import sys
import json
# 该接口为测试环境
SERVICE_NAME='com.testModule.frontServer'
OBJECT_PATH='/com/testModule/frontServer/object'
INTERFACE='com.testModule.frontServerInterface'
# 该接口为生产环境
# SERVICE_NAME='com.bmjc.ui'
# OBJECT_PATH='/bmjc/ui'
# INTERFACE='bmjc.ui'
def handleMsgFromUI():    
    arguments=sys.argv
    temp=arguments[1]
    temp=json.loads(temp)
    msgToUI={}
    msgToUI["scenename"]=str(temp["scenename"])
    msgToUI["functionname"]=str(temp["functionname"])
    return msgToUI
class CommHandler:
    def __init__(self):
        pass   
        
    def orgDataReportMsg(self,dataMsgPara):
        dataReportMsg=handleMsgFromUI()
        dataReportMsg["resulttype"]="datareport"
        dataReportMsg["result"]=dataMsgPara  
        return json.dumps(dataReportMsg)
    
    def orgErrReportMsg(self,errordescritionPara):
        errReportMsg=handleMsgFromUI()
        errReportMsg["resulttype"]="errorreport"
        resultTemp={}
        resultTemp["errordescrition"]=str(errordescritionPara)
        errReportMsg["result"]=resultTemp  
        return json.dumps(errReportMsg)
    
    def orgProgReportMsg(self,currentcompletionPara,currentstatusPara):
        progReportMsg=handleMsgFromUI()
        progReportMsg["resulttype"]="progressreport"
        resultTemp={}
        resultTemp["currentcompletion"]=str(currentcompletionPara)
        resultTemp["currentstatus"]=str(currentstatusPara)
        progReportMsg["result"]=resultTemp  
        return json.dumps(progReportMsg)
    
    def sendMsgToUI(self, resultMsgPara):        
        bus =dbus.SessionBus()
        obj = bus.get_object(SERVICE_NAME,OBJECT_PATH)
        iface =dbus.Interface(obj,INTERFACE)        
        print "backends向UI发送信息:"+str(resultMsgPara)  
        responseMsgFromUI = iface.updateFromTool(resultMsgPara) 
        print "backends收到UI响应信息:"+str(responseMsgFromUI)      