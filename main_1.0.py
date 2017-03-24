#!/usr/bin/python
# encoding:utf8
import random


class 居民(object):
    def __init__(self, 种族=None, 性别=None, 姓名=None, 阵营=None, 力量=None, 敏捷=None, 体质=None, 智力=None, 感知=None, 魅力=None,
                 运动=None, 特技=None, 手法=None, 隐匿=None, 奥秘=None, 历史=None, 自然=None, 宗教=None, 调查=None, 驯养=None, 洞悉=None,
                 医学=None, 观察=None, 生存=None,
                 欺诈=None, 威吓=None, 表演=None, 说服=None, 生活方式=None, 职业=None
                 ):
        self.职业 = 职业
        self.说服 = 说服
        self.表演 = 表演
        self.威吓 = 威吓
        self.欺诈 = 欺诈
        self.生存 = 生存
        self.观察 = 观察
        self.医学 = 医学
        self.洞悉 = 洞悉
        self.驯养 = 驯养
        self.调查 = 调查
        self.宗教 = 宗教
        self.自然 = 自然
        self.历史 = 历史
        self.奥秘 = 奥秘
        self.隐匿 = 隐匿
        self.手法 = 手法
        self.特技 = 特技
        self.运动 = 运动
        self.魅力 = 魅力
        self.感知 = 感知
        self.智力 = 智力
        self.体质 = 体质
        self.生活方式 = 生活方式
        self.敏捷 = 敏捷
        self.阵营 = 阵营
        self.姓名 = 姓名
        self.性别 = 性别
        self.种族 = 种族
        self.力量 = 力量


伊陆斯坎人类姓 = ['布莱特伍德', '赫尔德', '霍尔雷文', '拉克曼', '斯托维恩', '文德瑞瓦']
伊陆斯坎人类男名 = ['安德', '布拉特', '布兰', '夫拉夫', '盖斯', '兰德', '鲁特', '马尔瑟',
            '斯托尔',
            '塔曼', '厄斯']
伊陆斯坎人类女名 = ['阿玛芙丽', '贝塔', '瑟菲莉', '凯芙拉', '玛拉', '奥尔加', '斯莉芙里',
            '维丝特拉']


def 姓名生成器(种族, 性别):
    if 种族 == '人类':
        if 性别 == '男':
            姓名 = random.choice(伊陆斯坎人类姓) + '.' + random.choice(伊陆斯坎人类男名)
            return 姓名
        姓名 = random.choice(伊陆斯坎人类姓) + '.' + random.choice(伊陆斯坎人类女名)
        return 姓名
    print('未知种族')
性别统计表={'男':0,'女':0}
for x in range(2000000):
    a=random.choice(['男','女'])
    if a == '男':
        性别统计表['男']=性别统计表['男']+1
    else:
        性别统计表['女']=性别统计表['女']+1

print(性别统计表)
# a1 = 居民(姓名=姓名生成器(种族='人类', 性别='男'), 性别='男')
# a2 = 居民(姓名=姓名生成器(种族='人类', 性别='女'), 性别='女')

# print('姓名：%s ,性别：%s' % (a1.姓名, a1.性别))
# print('姓名：%s ,性别：%s' % (a2.姓名, a2.性别))
