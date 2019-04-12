# -*- coding: utf-8 -*-

class A:
    def spam(self):
        print('A.spam')
        
class B(A):
    def spam(self):
        print('B.spam')
        super().spam() # Call parent spam()
        
# super() 函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化了：
        
class A:
    def __init__(self):
        self.x = 0
        
class B(A):
    def __init__(self):
        super().__init__
        self.y = 1
        
# super() 的另外一个常见用法出现在覆盖Python特殊方法的代码中，比如：

class Proxy:
    def __init__(self, obj):
        self._obj = obj
    
    # Delegate attribute lookup to internal obj
    def __getattr__(self, name):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value) # Call original __setattr__
        else:
            setattr(self._obj, name, value)
            
    # 在上面代码中，setattr() 的实现包含一个名字检查。 如果某个属性名以下划线(_)开头，
    # 就通过 super() 调用原始的 setattr() ， 否则的话就委派给内部的代理对象 self._obj 
    # 去处理。 这看上去有点意思，因为就算没有显式的指明某个类的父类， 
    # super() 仍然可以有效的工作。
        