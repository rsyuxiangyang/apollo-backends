#!/usr/bin/env python
#-*-coding:utf-8-*- 
import gobject
# import dbus
import dbus.service
import dbus.mainloop.glib
import json
import os
import signal
SERVICE_NAME="com.bmjc.backend"
OBJECT_PATH="/bmjc/backend"
INTERFACE="bmjc.backend"
mainloop=None
def chldhandler(signum ,stackframe):
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)    
        except:
            print '.............'
            break
    
def runSubProcess(strFilePath,jsonRecipient,program, *args):
    signal.signal(signal.SIGCHLD, chldhandler)
    pid = os.fork()
    if not pid: 
        os.execl( "/usr/bin/python2.7", "python",strFilePath,jsonRecipient)     
    return "service has received"

def Exit():
        mainloop.quit() 

class DemoException(dbus.DBusException):
    _dbus_error_name = 'com.apollo.DemoException'

class BackServerObject(dbus.service.Object):
    @dbus.service.method(INTERFACE,in_signature='', out_signature='')
    def RaiseException(self):
        raise DemoException('The RaiseException method does what you might '
                            'expect')
        
    @dbus.service.method(INTERFACE,in_signature='s', out_signature='s')
    def reveiveFromUI(self,jsonRecipient):
        strPath=os.getcwd()[:len(os.getcwd())-10]+'backends/'#取刨除当前项目实际路径
        strRecipient = json.loads(jsonRecipient) #前端UI请求报文
        action=strRecipient["action"]            #以action为分界点判断   
        if "run"==action:
            scenename=strRecipient["scenename"] 
            functionname=strRecipient["functionname"]
            parameters={}
            parameters=strRecipient["parameters"]
        if "systeminfocheck"==functionname:
            strFilePath=strPath+'systemSecurityInfo/systemProcess.py'  
            runSubProcess(strFilePath,jsonRecipient,"python")                
        elif "stop"==action:
            print "stop"           
        elif "stopall"==action:
            print os.getpid()                       
        print '接收报文成功..'
        return "receive message success.."  

if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)    
    session_bus = dbus.SessionBus()
    name = dbus.service.BusName(SERVICE_NAME, session_bus)
    object = BackServerObject(session_bus,OBJECT_PATH)
    mainloop = gobject.MainLoop() 
    print "backServer start success..."
    mainloop.run()