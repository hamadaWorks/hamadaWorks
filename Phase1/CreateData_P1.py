# -*- coding: utf-8 -*-

"""
AI用のデータを作成する。

"""


import sqlite3
import random


DEF_DB_FILE = '../DB/DB_PHASE_1.sqlite3'
DEF_SQL_CREATE_P1 = """
CREATE TABLE T_PATTERN_1 (
    ID TEXT PRIMARY KEY,
    LABEL TEXT,
    P01 TEXT,
    P02 TEXT,
    P03 TEXT,
    P04 TEXT,
    P05 TEXT,
    P06 TEXT,
    P07 TEXT,
    P08 TEXT,
    P09 TEXT,
    P10 TEXT,
    P11 TEXT,
    P12 TEXT,
    P13 TEXT,
    P14 TEXT,
    P15 TEXT,
    P16 TEXT,
    P17 TEXT,
    P18 TEXT
)
"""

DEF_SQL_INSERT_P1 = """
INSERT INTO T_PATTERN_1 (
    ID,
    LABEL,
    P01,
    P02,
    P03,
    P04,
    P05,
    P06,
    P07,
    P08,
    P09,
    P10,
    P11,
    P12,
    P13,
    P14,
    P15,
    P16,
    P17,
    P18
) VALUES (
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?,
    ?
)
"""



DEF_GROUP_NUM = 6
DEF_GROUP_DATA_NUM = 10
DEF_GROUP_BIN_LEN = 3

MinNum = 0
MaxNum = 2 ** (DEF_GROUP_BIN_LEN - 1) - 2
insertData = '1' * DEF_GROUP_BIN_LEN

dataList = []

for indexInsert in range(DEF_GROUP_NUM):
    for indexDt in range(DEF_GROUP_DATA_NUM):
        dataArray = []
        dataArray.append('ID' + str(indexInsert) + '{0:010d}'.format(indexDt))
        dataArray.append(str(indexInsert))
        dataStr = ''
        for indexGrp in range(DEF_GROUP_NUM):
            if indexInsert == indexGrp:
                dataStr = dataStr + insertData
            else:
                rnum = random.randint(MinNum, MaxNum)
                rnumBin = bin(rnum)[2:len(bin(rnum))]
                rnumBin = ('0' * (DEF_GROUP_BIN_LEN - len(rnumBin))) + rnumBin
                dataStr = dataStr + rnumBin

        print('dataStr : {0}'.format(dataStr))
        dataArray.extend(list(dataStr))
        dataList.append(dataArray)

print('dataList: {0}'.format(dataList))














