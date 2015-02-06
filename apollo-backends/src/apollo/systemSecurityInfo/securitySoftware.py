#! /usr/bin/python
#-*-coding:utf-8-*- 
from apollo import commHandler
class SecuritySoftware(commHandler.CommHandler):
    def __init__(self):
        commHandler.CommHandler.__init__(self)
        pass 
    def getSecuritySoftware(self):
        return ""
if __name__ == "__main__":
    objectTemp=SecuritySoftware()  
    try: 
        raise Exception               
        dataReportMsg=objectTemp.orgDataReportMsg(objectTemp.getSecuritySoftware())
        objectTemp.sendMsgToUI(dataReportMsg)
        
        progReportMsg=objectTemp.orgProgReportMsg("100", "check the securitySoftware completed.")
        objectTemp.sendMsgToUI(progReportMsg)
    except Exception,e: 
        print e
        print "检查安全软件信息出错." 
        errReportMsg=objectTemp.orgErrReportMsg("check the securitySoftware error.")
        objectTemp.sendMsgToUI(errReportMsg)
