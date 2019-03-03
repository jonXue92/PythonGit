class MyException(Exception):
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message 

a=int(input("please input a num:"))
if a<10:
    try:
        raise MyException("my excepition is raised ")
    except MyException as e:
        print(e.message)