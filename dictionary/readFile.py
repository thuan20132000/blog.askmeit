import datetime
import os

 
with open(os.path.abspath(os.getcwd())+'dictionary/dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))
