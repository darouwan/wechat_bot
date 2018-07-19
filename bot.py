from wxpy import *
import time
# 初始化机器人，扫码登陆
bot = Bot()
aosong_group = bot.groups().search('澳宋荣光')[0]

while True:
    aosong_group.send("机器人：群还没沉")
    time.sleep(60)

