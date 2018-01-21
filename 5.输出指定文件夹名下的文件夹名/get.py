import os,sys

def visitDir(path):
    for lists in os.listdir(path):
        subPath = os.path.join(path,lists)
        if u'失败' in lists:
            for subLists in os.listdir(subPath):
                nextPath = os.path.join(subPath,subLists)
                for lastLists in os.listdir(nextPath):
                    lastPath = os.path.join(nextPath,lastLists)
                    f = open('Sum.txt','a')
                    f.write("%s\n" % lastLists)
                    f.close()
                    
def ndel(path):
    for lists in os.listdir(path):
        nextPath = os.path.join(path,lists)
        if os.path.isfile(nextPath):
            filePath = os.path.spilt(nextPath)
            sol = filePath[1].spilt('.')
            fileExt = sol[-1]
            if fileExt == 'txt':
                print (nextPath)
                f = open(nextPath,'r')
                res = open('Result.txt','a')
                res_list = []
                res_dup = []
                index = 0
                for line in f.readlines():
                    index = index + 1
                    if line in res_list:
                        temp_str = ""  
                        temp_str = temp_str + str(index)                   
                        temp_line = ''.join(line)  
                        temp_str = temp_str+temp_line  
                        res.write(temp_str); 
                    else:
                        res_list.append(line)
                f.close()
                res.close()
                    

#path = input('输入要添加的路径 ：').strip()
#path = 'F:\\5.统计指定文件夹中并输出excel'
path = os.getcwd()
visitDir(path)
ndel(path)
