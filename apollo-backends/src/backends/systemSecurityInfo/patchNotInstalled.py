#! /usr/bin/python
#-*-coding:utf-8-*- 
import os
from backends import father
class PatchNotInstalled(father.Father):
    def __init__(self):
        father.Father.__init__(self)
        pass 
    def getPatchNotInstalledInfo(self):
        return ""
if __name__ == "__main__":
    temp=PatchNotInstalled()
    temp.sendMsgToUI(temp.getPatchNotInstalledInfo())