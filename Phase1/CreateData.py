# -*- coding: utf-8 -*-

"""
AI用のデータを作成する。

"""


import sqlite3
import random

DEF_BIT_KT = 15

MinNum = 0
MaxNum = 2 ** DEF_BIT_KT

print('Min No : {0}'.format(MinNum))
print('Max No : {0}'.format(MaxNum))

rnum = random.randint(MinNum, MaxNum)
print('Random No : {0}'.format(rnum))

binStr = bin(rnum)
print('Max No (bin) : {0}'.format(binStr))

binStr = binStr[2:len(binStr)]
print('Max No (bin2) : {0}'.format(binStr))

print('len(binStr) : {0}'.format(len(binStr)))
print('len(binStr)2 : {0}'.format(30 - len(binStr)))

zeroStr = '0' * (DEF_BIT_KT - len(binStr))
print('zeroStr : {0}'.format(zeroStr))

binStr = '{0}{1}'.format(zeroStr, binStr)
print('Max No (bin2) : {0}'.format(binStr))

insertStart = 6
insertDataLen = 3
insertData = '111'

beforeBin = binStr[0:insertStart]
afterBin = binStr[insertStart:DEF_BIT_KT]
print('beforeBin : {0}'.format(beforeBin))
print('beforeAfter : {0}'.format(afterBin))

binData = ''.join([beforeBin, insertData, afterBin])
print('binData : {0}'.format(binData))

binList = list(binData)
print('binData : {0}'.format(binList))








