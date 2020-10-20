import re
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

from dingtalkchatbot.chatbot import DingtalkChatbot
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=81355aec2d36297d67978f3db1fe8d54819cb498bae833d0ad87dc4a6bb1237e'		# WebHook地址
xiaoding = DingtalkChatbot(webhook)		# 初始化机器人小丁

#发送文字消息
xiaoding.send_text(msg='通知：不治将恐深', is_at_all=True)



