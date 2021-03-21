import datetime
 
with open('/Users/truongthuan/Develop/python/blog/dictionary/dateInfo.txt','a') as outFile:
    outFile.write('\n' + str(datetime.datetime.now()))
