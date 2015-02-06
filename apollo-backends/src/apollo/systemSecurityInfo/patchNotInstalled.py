#! /usr/bin/python
#-*-coding:utf-8-*- 
from apollo import commHandler
from common.utils.log4py import log4py
class PatchNotInstalled(commHandler.CommHandler):
    def __init__(self):
        commHandler.CommHandler.__init__(self)
        pass 
    def getPatchNotInstalled(self):
        return ""
if __name__ == "__main__":    
    objectTemp=PatchNotInstalled()
    try:
        raise Exception        
        dataReportMsg=objectTemp.orgDataReportMsg(objectTemp.getPatchNotInstalled())
        objectTemp.sendMsgToUI(dataReportMsg)
        
        progReportMsg=objectTemp.orgProgReportMsg("100", "check the patchNotInstalled completed.")
        objectTemp.sendMsgToUI(progReportMsg)
    except Exception,e: 
        print e
        print "检查未安装补丁信息出错." 
        log4py.error('errorrrrrrrrrrrrrrr')
        errReportMsg=objectTemp.orgErrReportMsg("check the patchNotInstalled error.")
        objectTemp.sendMsgToUI(errReportMsg)
