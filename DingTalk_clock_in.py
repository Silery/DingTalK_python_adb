import os
import time
x = 0
dict_user =[
            {"username":"13606586792","passwd":"gmh123.0"},
           ]



#点击
def click(x,y):
    time.sleep(0.5)
    os.system('adb shell input tap {x} {y}'.format(x=x,y=y))
    time.sleep(0.5)
#左滑
def swipe_left():
    os.system('adb shell input swipe 700 1400 900 1400')
    time.sleep(0.5)
def swipe_up(x1,y1,x2,y2):
    time.sleep(0.5)
    os.system('adb shell input swipe {x1} {y1} {x2} {y2}'.format(x1=x1,y1=y1,x2=x2,y2=y2))
    time.sleep(0.5)
#右滑
def swipe_right():
    os.system('adb shell input swipe 900 1400 700 1400')
    time.sleep(0.5)
def input(txt):

    time.sleep(0.5)
    os.system('adb shell input text {}'.format(txt))
    time.sleep(0.5)

# username  = r"13606586792"
passwd = "gmh123.0"
swipe_right()
#打开钉钉
print("打开钉钉")
click(902,1045)
time.sleep(2)
for i in dict_user:
    x = x+1
    print("第{}次登录测试！！！！！！！！！！！！".format(x))
    #清空并输入账号
    click(560,623)
    click(962,603)
    print("输入账号")

    input(i["username"][0:4])
    input(i["username"][4:8])
    input(i["username"][8:11])
    #输入密码
    print("输入密码")
    click(381,810)
    input(i["passwd"])
    #同意协议
    click(114,1182)
    #登录
    click(534,970)
    time.sleep(2)
    #登录
    # print("登录")
    # click(100,910)
    # time.sleep(5)
    #找到工作区，点击打卡
    click(510,2150)
    time.sleep(2)
    click(113,960)
    #具体打卡

    '''    
    '''
    #点击今天
    time.sleep(2)
    click(100,1500)
    time.sleep(2)
    #往下滑到最底
    swipe_up(100,2100,100,100)
    swipe_up(100,2100,100,100)
    # 点击获取地址
    click(1013,1546)
    swipe_up(100,2100,100,1500)
    # 点击提交
    click(588,2160)
    print("打卡成功")
    #退出回到信息栏
    click(80,130)
    click(200,150)
    #点击我的
    click(980,2200)
    #完成之后退出 账号
    #点击设置
    click(730,1850)
    #滑到底部点击退出登录
    swipe_up(100,2100,100,1500)
    click(550,2050)

    #退出登录
    click(810,1230)
    time.sleep(2)
    # #确定
    # click(730,1200)
    print("退出登录")