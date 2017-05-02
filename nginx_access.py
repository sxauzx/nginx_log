#!/usr/bin/python

import os
import fileinput
import re

dir_log = r"/root/access.log"

ipP = r"?P<ip>[\d.]*"
timeP = r"?P<time>\[[^\[\]]*\]"
requestP = r'?P<request>\"[^\"]*\"'
statusP = r"?P<status>\d+"
bodyBytesSentP = r"?P<bodyBytesSent>\d+"
referP = r'?P<refer>\"[^\"]*\"'
userAgentP = r'?P<userAgent>\"[^\"]*\"'

nginxLogPattern = re.compile(r"(%s)\ -\ -\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)\ (%s)" %(ipP, timeP, requestP, statusP, bodyBytesSentP, referP, userAgentP), re.VERBOSE)

def processLog(dir_log):
    for line in fileinput.input(dir_log):
        matchs = nginxLogPattern.match(line)
        if matchs !=None:
            allGroups = matchs.groups()
            ip = allGroups[0]
            time = allGroups[1]
            request = allGroups[2]
            status = allGroups[3]
            bodyBytesSent = allGroups[4]
            refer = allGroups[5]
            userAgent = allGroups[6]
#            userAgent = matchs.group("userAgent")
            GetResponseStatusCount(userAgent)
        else:
            raise Exception
    fileinput.close()

allStatusDict = {}
def GetResponseStatusCount(status):
    if allStatusDict.has_key(status):
        allStatusDict[status] += 1
    else:
        allStatusDict[status] = 1;

if __name__ == "__main__":
    processLog(dir_log)
    print allStatusDict
