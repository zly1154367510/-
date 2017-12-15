#coding=utf-8
import sys
import json
reload(sys)
sys.setdefaultencoding("GB18030")
from matplotlib.pyplot import plot
import pandas as pd
'''
0:身高
1：网民
2：岁数
3：婚姻情况
4：所在地区
'''
maritalStatusList = []
locationList = []
'''
统计婚姻情况占比
maritalStatusList
地区占比
locationList
年龄列表
ageList
int化age列表
ageIntList
'''

d = pd.read_csv("dgData.csv")
'''
柱形图
'''
# maritalStatusList = pd.DataFrame(d.groupby("3").count()["2"])
# XmaritalStatusList = list(maritalStatusList.index)
# YmaritalStatusList = list(maritalStatusList["2"])
#
# locationList = pd.DataFrame(d.groupby("4").count()["2"])
# XlocationList = list(locationList.index)
# YlocationList = list(locationList["2"])
#
# ageList = pd.DataFrame(d.groupby("2").count()[["2"]])
# XageList = list(ageList.index)
# YageList = list(ageList["2"])
#
'''
饼形图
'''
# ageIntList = []
# for i in d["2"]:
#     i = i.replace("岁","")
#     ageIntList.append(int(i))
# ageDF = pd.DataFrame(ageIntList,columns=["age"])
# XageList = ['少年','青年','中年']
# YageList = []
# YageList.append(ageDF[ageDF[ageDF.age>14]<20].count())
# YageList.append(ageDF[ageDF[ageDF.age>19]<35].count())
# YageList.append(ageDF[ageDF[ageDF.age>34]<60].count())







