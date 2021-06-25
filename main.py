#!/bin/env python3
# -*-coding:utf8-*-
import re
from json import loads

from flask import Flask, request

from func import *
from send import *

bot_server = Flask(__name__)
# 管理员列表 （可不用设置）
suList = ['1782898491']
# 定义一些字符串变量
text, image, record, video, location = 'text', 'image', 'record', 'video', 'location'


@bot_server.route('/api/message', methods=['POST'])
# 路径是你在酷Q配置文件里自定义的
def server():
    '''主要函数'''
    data = request.get_data().decode('utf-8')
    data = loads(data)

    if 'status' not in data:
        # 打印原始详细内容
        print('原始详细内容：', data)
        # 去掉开头第一个字符后的接收消息
        msg = data['raw_message'][1:]  # 消息内容
        # 打印
        print('去掉开头第一个字符后的接收消息：', msg,)

        # 消息类型 group private
        message_type = data['message_type']
        # 发送者
        user_id      = str(data['user_id'])

        # 如果消息是私人消息
        if message_type == 'private':
            # 判断消息发送者是否是管理员
            if user_id in suList:
                if msg == '你好':
                    send('你好')

        # 如果消息是群消息
        elif message_type == 'private':
            # 定义发送群
            group_id = str(data['group_id'])


    return ''

if __name__ == '__main__':
    bot_server.run(port=5701)
    # 端口也是配置文件里自定义的


