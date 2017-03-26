#!/usr/bin/python
# encoding:utf8
import random
import heapq
import sqlalchemy
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, insert, create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

# 创建对象基类


Base = declarative_base()


class 居民(Base):
    __tabname__ = '居民'

    id = Column(Integer, primary_key=True)
    阵营 = Column(String)
    姓名 = Column(String)
    性别 = Column(String)
    种族 = Column(String)
    职业 = Column(String)
    魅力 = Column(Integer)
    感知 = Column(Integer)
    智力 = Column(Integer)
    体质 = Column(Integer)
    敏捷 = Column(Integer)
    力量 = Column(Integer)
    说服 = Column(Integer)
    表演 = Column(Integer)
    威吓 = Column(Integer)
    欺诈 = Column(Integer)
    生存 = Column(Integer)
    观察 = Column(Integer)
    医学 = Column(Integer)
    洞悉 = Column(Integer)
    驯养 = Column(Integer)
    调查 = Column(Integer)
    宗教 = Column(Integer)
    自然 = Column(Integer)
    历史 = Column(Integer)
    奥秘 = Column(Integer)
    隐匿 = Column(Integer)
    手法 = Column(Integer)
    特技 = Column(Integer)
    运动 = Column(Integer)
    生活方式 = Column(String)


class 居民(object):
    def __init__(self, 编号=None, 种族=None, 性别=None, 姓名=None, 阵营=None, 力量=None, 敏捷=None, 体质=None, 智力=None, 感知=None,
                 魅力=None,
                 运动=None, 特技=None, 手法=None, 隐匿=None, 奥秘=None, 历史=None, 自然=None, 宗教=None, 调查=None, 驯养=None, 洞悉=None,
                 医学=None, 观察=None, 生存=None,
                 欺诈=None, 威吓=None, 表演=None, 说服=None, 生活方式=None, 职业=None
                 ):
        self.编号 = 编号
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

种族列表=['矮人','精灵','半身人','人类','龙裔','侏儒','半精灵','半兽人','提夫林']
伊陆斯坎人类姓 = ['布莱特伍德', '赫尔德', '霍尔雷文', '拉克曼', '斯托维恩', '文德瑞瓦']
伊陆斯坎人类男名 = ['安德', '布拉特', '布兰', '夫拉夫', '盖斯', '兰德', '鲁特', '马尔瑟',
            '斯托尔',
            '塔曼', '厄斯']
伊陆斯坎人类女名 = ['阿玛芙丽', '贝塔', '瑟菲莉', '凯芙拉', '玛拉', '奥尔加', '斯莉芙里',
            '维丝特拉']

def 种族生成器(种族):
    return random.choice(种族)


def 性别生成器(性别):
    return random.choice(性别)

def 职业生成器(职业):
    return random.choice(职业)

def 属性生成器(STR=1,DEX=1,CON=1,INT=1,WIS=1,CHA=1):
    Roll_number=1
    Roll_result=[]
    while Roll_number <4:
        Roll_result.append(random.randrange(1,6))
        Roll_number=Roll_number+1
    STR=sum(heapq.nlargest(3,Roll_result))
    Roll_number=1
    Roll_result=[]
    while Roll_number <4:
        Roll_result.append(random.randrange(1,6))
        Roll_number=Roll_number+1
    DEX=sum(heapq.nlargest(3,Roll_result))
    Roll_number=1
    Roll_result=[]
    while Roll_number <4:
        Roll_result.append(random.randrange(1,6))
        Roll_number=Roll_number+1
    CON=sum(heapq.nlargest(3,Roll_result))
    Roll_number=1
    Roll_result=[]
    while Roll_number <4:
        Roll_result.append(random.randrange(1,6))
        Roll_number=Roll_number+1
    INT=sum(heapq.nlargest(3,Roll_result))
    Roll_number=1
    Roll_result=[]
    while Roll_number <4:
        Roll_result.append(random.randrange(1,6))
        Roll_number=Roll_number+1
    WIS=sum(heapq.nlargest(3,Roll_result))
    Roll_number=1
    Roll_result=[]
    while Roll_number <4:
        Roll_result.append(random.randrange(1,6))
        Roll_number=Roll_number+1
    CHA=sum(heapq.nlargest(3,Roll_result))
    return STR, DEX, CON, INT, WIS, CHA

def 属性生成器2(STR=1,DEX=1,CON=1,INT=1,WIS=1,CHA=1):
    Roll_list={'STR':0, 'DEX':0, 'CON':0, 'INT':0, 'WIS':0, 'CHA':0}
    for x in Roll_list:
        Roll_number = 1
        Roll_result = []
        while Roll_number < 4:
            Roll_result.append(random.randrange(1, 6))
            Roll_number = Roll_number + 1
        Roll_list[x] = sum(heapq.nlargest(3, Roll_result))
    return Roll_list


def 姓名生成器(性别):
    if 性别 == '男':
        姓名 = random.choice(伊陆斯坎人类男名) + '.' + random.choice(伊陆斯坎人类姓)
        return 姓名
    性别 = random.choice(伊陆斯坎人类女名) + '.' + random.choice(伊陆斯坎人类姓)
    return 姓名
姓名统计表 = []
for x in range(10000):
    a = random.choice(['男', '女'])
    姓名统计表.append([姓名生成器(a), a])

for x in 姓名统计表:
    print(x)
# a1 = 居民(姓名=姓名生成器(种族='人类', 性别='男'), 性别='男')
# a2 = 居民(姓名=姓名生成器(种族='人类', 性别='女'), 性别='女')

# print('姓名：%s ,性别：%s' % (a1.姓名, a1.性别))
# print('姓名：%s ,性别：%s' % (a2.姓名, a2.性别))
