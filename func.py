#!/bin/env python3
# -*-coding:utf8-*-

import re
import time

import requests


def alapi(api, other=''):
    '''
    一言　　 'hitokoto' \n
    毒鸡汤　 'soul' \n
    舔狗日记 'dog' \n
    诗词　　 'shici' \n
    笑话　　 'joke/random' \n
    美文　　 'mryw/random' \n
    歇后语　 'xhy/random' \n
    早报　　 'zaobao' \n
    历史今天 'eventHistory' \n
    谜语　　 'riddle/random' \n\n
    ACG图片　'acg' \n
    必应日图 'bing' \n
    字典　　 'word', '字' \n
    词典　　 'ciword', '词典' \n
    成语　　 'idiom', '成语' \n
    帮助　　 help 
    '''
    # 去 https://www.alapi.cn 申请token
    token = '' 
    api_url = f'https://v2.alapi.cn/api/{api}?token={token}'
    response = ''

    # 帮助
    if api == 'help':
        return '目前已实现功能如下\n！一言\n！毒鸡汤\n！舔狗日记\n！诗词\n！笑话\n！美文\n！歇后语\n！早报\n！历史今天\n！谜语\n！ACG图片\n！必应日图\n！字典 字\n！词典 词语\n！成语 四字成语\n！6位基金代码  查询基金估值'
    # 一言
    elif api == 'hitokoto':
        return requests.get(api_url).json()['data']['hitokoto']
    # 毒鸡汤 舔狗日记 诗词 笑话
    elif api in ['soul', 'dog', 'shici', 'joke/random']:
        return requests.get(api_url).json()['data']['content']
    # 美文
    elif api == 'mryw/random':
        r = requests.get(api_url).json()['data']
        title = r['title']
        author = r['author']
        content = r['content'].replace('</p>', '\n').replace('<p>', '')
        return f"{title}\n{author}\n\n{content}"
    # 歇后语
    elif api == 'xhy/random':
        r = requests.get(api_url).json()['data']
        riddle = r['riddle']
        answer = r['answer']
        return f'{riddle}\n　　——{answer}'
    # 60秒读懂世界
    elif api == 'zaobao':
        return f'{api_url}&format=image'
    # ACG 必应
    elif api in ['acg', 'bing']:
        return requests.get(f'{api_url}&format=json').json()['data']['url']
    # 历史今天
    elif api == 'eventHistory':
        r = requests.get(api_url).json()['data']
        for i in range(len(r)):
            response += r[i]['date'] + '\n' + r[i]['title'] + '\n\n'
        return response
    # 谜语 'type=ciyumiyu'
    elif api == 'riddle/random':
        r = requests.get(f'{api_url}&type=ciyumiyu').json()['data']
        content = r['content']
        answer = r['answer']
        return f'问：{content}\n答：{answer}'
    # 字典
    elif api == 'word':
        r = requests.get(f'{api_url}&word={other}').json()['data']
        if r == None:
            return '好猛啊，无法查询这个字，请更换！'
        old_word = r['old_word']
        strokes = r['strokes']
        pinyin = r['pinyin']
        explanation = r['explanation']
        return response + f'{word} 读音：{pinyin} 笔画：{strokes} 繁体：{old_word}\n解释：{explanation}'
    # 词典
    elif api == 'ciword':
        r = requests.get(f'{api_url}&word={other}').json()['data'][0]
        word = r['word']
        if word == other:
            response = ''
        else:
            response = f'未查询到{other}，匹配到如下词语：\n'
        pinyin = r['pinyin']
        explanation = r['explanation']
        return response + f'{word} 读音：{pinyin}\n解释：{explanation}\n'
    # 成语
    elif api == 'idiom':
        print(other)
        r = requests.get(f'{api_url}&word={other}').json()['data'][0]
        word = r['word']
        if word == other:
            response = ''
        else:
            response = f'未查询到{other}，匹配到如下词语：\n'
        pinyin = r['pinyin']
        explanation = r['explanation']
        derivation = r['derivation']
        example = r['example']
        return response + f'{word} 读音：{pinyin}\n解释：{explanation}\n出自：{derivation}\n例子：{example}'
    # 定位
    elif api == 'ip':
        r = requests.get(f'{api_url}&ip={other}').json()['data']
        lat = r['location']['lat']
        lng = r['location']['lng']
        gps_png = f'http://apis.map.qq.com/ws/staticmap/v2/?key=RJNBZ-56724-USWUA-XVB56-RWETV-AIBPS&size=720x360&zoom=14&no_logo=1&scale=2&markers=size:mid|color:red|label:k|{lat},{lng}&center={lat},{lng}'
        pos = r['pos'] + '  ' + r['isp']
        return gps_png, pos
    # 短网址
    elif api == 'url':
        return requests.get(f'{api_url}&type=tcn&url={other}').json()['data']['short_url']
    # 文字转二维码
    elif api == 'qr':
        return requests.get(f'{api_url}&return=raw&content={other}')
        # return requests.get(f'{api_url}&return=json&content={other}').json()['data']['short_url']

# print(alapi('acg','format=json'))


def bot_qingyunke(msg):
    '''青云客智能聊天'''
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + msg
    return requests.get(url).json()['content'].replace('{br}', '\n')


def fund():
    '''基金查询，无参数'''
    # 基金列表，仅供娱乐
    fundList = [
        ["农银", "002190", 1000],
        ["建信", "009147", 1000],
        ["白酒", "161725", 1000],
        ["前海", "002079", 1000],
        ["兴全", "001511", 1000],
        ["景顺", "260108", 1000]
    ]
    # 添加日期和时间
    result = time.strftime(
        "日期：%m月%d日 星期%w\n时间：%H:%M\n-----------------\n", time.localtime())
    all_jjgz = all_sygz = 0
    for fund in fundList:
        url = 'http://fundgz.1234567.com.cn/js/' + fund[1] + '.js'
        data = requests.get(url).text
        # 基金估值
        jjgz = float(re.findall('"gszzl":"(.*?)"', data)[0])
        sygz = jjgz * fund[2] * 0.01
        result += f"{fund[0]}：{jjgz:+.2f}  {sygz:+.0f}\n"

        all_jjgz += jjgz
        all_sygz += sygz
    average_jjgz = all_jjgz / len(fundList)

    result += f"-----------------\n总计：{average_jjgz:+.2f}  {all_sygz:+.0f}"
    return result


def fund_img(fund_id):
    '''基金估值查询，6位数字'''
    return f"http://j4.dfcfw.com/charts/pic6/{fund_id}.png"

