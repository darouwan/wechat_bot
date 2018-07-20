from wxpy import *
import time
import datetime

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)
aosong_group = bot.groups().search('澳宋荣光')[0]


@bot.register([aosong_group], TEXT)
def auto_reply(msg):
    # 如果是群聊，但没有被 @，则不回复
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        print(msg.text)
        if msg.text.find('沉') >= 0:
            msg = "姜饼大官人播报：当前%s,群还没沉" % (time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())))
            aosong_group.send(msg)
            # 回复消息内容和类型


embed()
