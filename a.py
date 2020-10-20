# import re
# pattern = re.compile('http://www.tujigu.com')
# str = u'http://www.tujigu.com/a/155'
# print(pattern.search(str))

# str = u'http://www.tujigu.com/a/155/'

# print(str.split('/'))


# sources = {
#     "https://www.guancha.cn": 1,
#     "https://news.sina.com.cn/world/": 2,
#     "http://www.bjnews.com.cn/world/": 3,
#     'http://www.chinanews.com/world.shtml':4,

# }


# print(list(sources))
from datetime import datetime
print()
a=datetime.today().strftime('%Y-%m-%d %H:%M')
from dingtalkchatbot.chatbot import DingtalkChatbot,CardItem
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=81355aec2d36297d67978f3db1fe8d54819cb498bae833d0ad87dc4a6bb1237e'		# WebHook地址
secret = 'SEC31ae94c1e65c90cea577ce5b390412e1b5b6c3da7271e53f5fe1df52b6d89d05'
xiaoding = DingtalkChatbot(webhook, secret=secret)		# 初始化机器人小丁

#发送文字消息
xiaoding.send_text(msg=f'{a}:\n  爬取了200条新闻，过滤20条', is_at_all=False)

# # cards=[]
# card1 = CardItem(title='中国儿女', url='http://baidu,com', pic_url="https://i.loli.net/2020/10/20/hHPAjzSfZCceYvX.jpg")
# card2=CardItem(title='中国儿女', url='http://baidu,com', pic_url="https://i.loli.net/2020/10/20/hHPAjzSfZCceYvX.jpg")
# cards.append(card1)
# cards.append(card2)

# # xiaoding.send_text(msg=f'通知：{reason}\n'+t, is_at_all=True)
# # FeedCard消息类型
# xiaoding.send_feed_card(cards)


# a = '123123'
# b = f'sadkfjaslkdjfklsdfj{a}alksdjf'
# print(b)


# import itertools
# aa = ['a', 'b', 'c']
# bb = list(itertools.permutations(aa, 2))
# print(bb)
# print("######################")
# cc = list(itertools.combinations(aa, 2))
# print(cc[1][1])

# from twilio.rest import Client

# # Your Account SID from twilio.com/console
# account_sid = "AC10c6cac5e4c8f9d5d2898a8aff8ead9a"
# # Your Auth Token from twilio.com/console
# auth_token  = "1b2cd2993596a3d23d6f3bc83253fd23"

# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     to="+8615803482891", 
#     from_="+12673802837",
#     body="Hello from Python!")

# print(message.sid)
