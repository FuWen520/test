# coding = utf-8

'''
author:FuWen
email:heart3214@163.com
'''

import  poo
'''包 组织管理代码的方式，用于将模块放在一起的文件夹就是包
至少有一个__init__.py文件
'''
stu = poo.Student('xiaojing',19)
stu.say()
poo.sayhello()
poo.printer()

from poo import  Student,printer
stu = Student('xiaoyueyue',11)
stu.say()
poo.sayhello()
printer()

import  sys
'''模块的搜索路径'''
print(type(sys.path))
print(sys.path)
for p in sys.path:
    print(p)

def func(n):
    '''阶乘的计算，往下递送，往回归。必须有递有归。有结束条件'''
    if n == 1:
        return  1
    return  n * func(n-1)
print('100的阶乘为：',func(100))
printer()

def fib(n):
    '''斐波那契数列 ， 以资源换取时间。一定要有结束条件'''
    if n == 1 or n == 2:
        return  1
    return fib(n-1) + fib(n-2)
print('斐波那契数列 10：' ,fib(10))
printer()

a,b,c = 'A','B','C'
def hano(a,b,c,n):
    if n == 1:
        print('{} --> {}'.format(a,c))
        return None
    if n == 2:
        print('{} --> {}'.format(a,c))
        print('{} --> {}'.format(a,b))
        print('{} --> {}'.format(b,c))
        return None

    hano(a,c,b,n-1)
    print('{} --> {}'.format(a,c))
    hano(b,a,c,n-1)

print('只有一个盘子的情况：',hano(a,b,c,1))
print('只有二个盘子的情况：',hano(a,b,c,2))
print('只有三个盘子的情况：',hano(a,b,c,3))
print('只有10个盘子的情况：',hano(a,b,c,6))
printer()









