#! /usr/bin/python
#-*-coding:utf-8-*- 
import os
from backends import father
class SystemProcess(father.Father):
    def __init__(self):
        father.Father.__init__(self)
        pass 
    def getProcessInfo(self):
        hw = os.popen('ps -ef')
        processInfo = hw.read()
        hw.close()
        UID,PID,PPID,C,STIME,TTY,TIME,CMD = '','','','','','','',''
        tmp=[]
        processInfoTmp={}
        processInfoList=[]
        if processInfo :
            tmp = processInfo.split("\n")
            tmp.remove(tmp[0])
            for item in tmp:
                processInfoTmp={}
                UID=item[0:9]
                UID=UID.strip()
                processInfoTmp["UID"]=UID
#                 processInfoTmp.append(UID)                
                PID=item[9:16]
                PID=PID.strip()
                processInfoTmp["PID"]=PID
#                 processInfoTmp.append(PID)
                PPID=item[16:22]
                PPID=PPID.strip()
                processInfoTmp["PPID"]=PPID
#                 processInfoTmp.append(PPID)
#                 C=item[22:24]
#                 C=C.strip()
#                 processInfoTmp["C"]=C
#                 processInfoTmp.append(C)
                STIME=item[24:30]
                STIME=STIME.strip()
                processInfoTmp["STIME"]=STIME
#                 processInfoTmp.append(STIME)
                TTY=item[30:39]
                TTY=TTY.strip().replace("?", "none")
                processInfoTmp["TTY"]=TTY
#                 processInfoTmp.append(TTY)
                TIME=item[39:47]
                processInfoTmp["TIME"]=TIME
#                 processInfoTmp.append(TIME)
                CMD=item[48:]
                processInfoTmp["CMD"]=CMD
#                 processInfoTmp.append(CMD)
                processInfoList.append(processInfoTmp)                
#                 print UID   #用户ID               
#                 print PID   #进程ID
#                 print PPID  #父进程ID
#                 print C 
#                 print STIME #开始时间
#                 print TTY   #终端名称
#                 print TIME  #进程执行时间，进程启动所占用CPU时间
#                 print CMD   #命令行输入
#             print processInfoList
            return processInfoList
    def process_list(self):
        pids = []
        for subdir in os.listdir('/proc'):
            if subdir.isdigit():
                pids.append(subdir)
        return pids
if __name__ == "__main__":    
    temp=SystemProcess()
    temp.sendMsgToUI(temp.getProcessInfo())
