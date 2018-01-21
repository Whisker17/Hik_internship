import os,sys

def visitDir(path):
    for dirPath,subPath,fileName in os.walk(path):
        if u'失败' in dirPath and subPath != []:
            dirNames = dirPath.split('\\')
            for i in range(len(subPath)):
                #print ("%s %s\n" % (dirNames[-2],subPath[i]))
                f = open('Sum.txt','a')
                f.write("%s %s\n" % (dirNames[-2],subPath[i]))
                f.close()

path = os.getcwd()
visitDir(path)
