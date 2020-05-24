# coding = utf-8

'''
author:FuWen
email:heart3214@163.com
'''
class Student():
    def __init__(self,name = 'NoName',age=18):
        self.name = name
        self.age = age

    def say(self):
        print('My name is {0}'.format(self.name))

def sayhello():
    print('Hi,welcome to TuLing xueyuan!')
def printer():
    print('分割线'.center(60,'-'))

if __name__ == '__main__':
    print('我是poo吖，你叫我干哈')
    printer()