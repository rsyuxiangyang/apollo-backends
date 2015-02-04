#! /usr/bin/python
#-*-coding:utf-8-*- 
import os
from backends import father
class TimeSwitchMachine(father.Father):
    def __init__(self):
        father.Father.__init__(self)
        pass 
    def getTimeSwitchMachineInfo(self):
        return ""
if __name__ == "__main__":    
    temp=TimeSwitchMachine()
    temp.sendMsgToUI(temp.getTimeSwitchMachineInfo())
