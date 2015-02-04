#! /usr/bin/python
#-*-coding:utf-8-*- 
import os
from backends import father
class SecuritySoftware(father.Father):
    def __init__(self):
        father.Father.__init__(self)
        pass 
    def getSecuritySoftwareInfo(self):
        return ""
if __name__ == "__main__":
    temp=SecuritySoftware()
    temp.sendMsgToUI(temp.getSecuritySoftwareInfo())
