#!/usr/bin/env python

import dbus
import json
class MockClient:
    def mockRun(self):
        strRun={"action":"run",
                "scenename":"onekeycheck",
                "functionname":"systeminfocheck",         
                "parameters":{"parameter1":"S",
                              "parameter2":"S",
                              "parameter3":"S"}}
        strJsonRun=json.dumps(strRun)
        return strJsonRun
    def mockStop(self):
        strStop={"action":"run","scenename":"onekeycheck","functionname":"systeminfocheck",         
           "parameters":{
           "parameter1":"S",
           "parameter2":"S",
           "parameter3":"S"
                                }
              }
        strJsonstrStop=json.dumps(strStop)
        return strJsonstrStop
    def mockStopAll(self):
        strStopAll={"action":"run","scenename":"onekeycheck","functionname":"systeminfocheck",         
           "parameters":{
           "parameter1":"S",
           "parameter2":"S",
           "parameter3":"S"
                                }
                }
        strJsonStopAll=json.dumps(strStopAll)
        return strJsonStopAll
if __name__ == '__main__':
    bus =dbus.SessionBus()
    obj = bus.get_object('com.bmjc.backend','/bmjc/backend')
    iface =dbus.Interface(obj,'bmjc.backend') 
    mockClient=MockClient()
    serverResult = iface.reveiveFromUI(mockClient.mockRun());
    print "client1 received msgs:"+str(serverResult)

