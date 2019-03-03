if __name__ == '__main__':
    fname = input("Please input the file's name:")
    print(fname)

try:    #尝试执行一个或多个语句
    fobj = open(fname,"r")    #尝试打开一个文件
except IOError as error:      #如果无法执行"try"里面的语句,那么就执行except里面的语句  另外需要注意的是,"error"相当于是一个变量,用于存储错误信息的
    print ("*** file open error", error)                        #标准语句和相关信息。
else:   #如果try里面的语句成功执行,那么就执行else里面的语句
    for eachline in fobj:
        print(eachline,)
        fobj.close()
