import datetime
import os

 
with open('/Users/truongthuan/Develop/python/dictionary/dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))
