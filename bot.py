from wxpy import *
import time
import datetime

# 初始化机器人，扫码登陆
bot = Bot()
aosong_group = bot.groups().search('澳宋荣光')[0]

while True:
    msg = "姜饼大官人播报：当前%s,群还没沉" % (time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())))
    aosong_group.send(msg)
    print(msg)
    time.sleep(600)
