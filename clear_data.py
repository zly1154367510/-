#coding=utf-8
import sys
import json
reload(sys)
sys.setdefaultencoding("GB18030")
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
import pandas as pd
import numpy as np
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
身高
heightList
'''
def intToFloat(list1):
    list3 = []
    for i in list1:
        i = float(i)
        list3.append(i)
    return list3

def Columnar_graph(xList, yList, xLabel, yLabel, title):
    plt.barh(xList, yList)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    return plt

def pie_graph(xList, yList, title):
    plt.pie(yList, labels=xList, autopct='%3.1f %%')
    plt.title(title)
    return plt

d = pd.read_csv("dgData.csv")

'''
地区未婚人数占比
'''
# clearD = list(d.groupby("所在地区")["婚姻"])
# clearD1 =  list(d.groupby("所在地区")["婚姻"].count())#地区分组人数
clearLocationName = list(d.groupby("所在地区")["婚姻"].count().index)#地区名
#
# clearDogNumList = []#未婚数量
clearLocationName1 = []
for i in clearLocationName:
    i = i.replace(" ","")
    i = i.replace("市辖区","香港")
    i = i.replace("地级","普宁")

    clearLocationName1.append(i)
# for i in clearD:
#     clearDogNum = 0
#     for item in i:
#         for item1 in item:
#            if item1.find("未婚") != -1:
#                clearDogNum += 1
#     clearDogNumList.append(clearDogNum)
#
# npDogNum = np.array(intToFloat(clearDogNumList))
# npClearD1 = np.array(intToFloat(clearD1))
# dogProportion = npDogNum/npClearD1

'''
平均身高 按地区分组
'''
# intHeightList = []
# heightList = list(d.groupby("所在地区")["身高"])


# he = 0
# num = 0
# pingList = []
# for i in heightList:
#     for item in i:
#         for item1 in item:
#            if `item1`.find("cm") != -1:
#
#                num += 1
#                item1 = item1.replace("cm","")
#                he = he + float(item1)
#     pingList.append(he/num)


    # intHeightList.append(item)





'''
柱形图
'''
# maritalStatusList = pd.DataFrame(d.groupby("3").count()["2"])
# XmaritalStatusList = list(maritalStatusList.index)
# YmaritalStatusList = list(maritalStatusList["2"])

# locationList = pd.DataFrame(d.groupby("4").count()["2"])
# YlocationList = list(locationList.index)
# YlocationList1 = []
# for i in YlocationList:
#     i = i.replace("广东 ","")
#     i = i.replace("市辖区","未知")
#     i = i.replace("地级"," ")
#     YlocationList1.append(i)# YlocationList1 = []
# for i in YlocationList:
#     i = i.replace("广东 ","")
#     i = i.replace("市辖区","未知")
#     i = i.replace("地级"," ")
#     YlocationList1.append(i)
#
# XlocationList = list(locationList["2"])

# ageList = pd.DataFrame(d.groupby("2").count()[["2"]])
# XageList = list(ageList.index)
# YageList = list(ageList["2"])
#

'''
折线图
'''

# heightList = pd.DataFrame(d.groupby("0").count()["2"])
# XheightList = list(heightList.index)
# XheightList1 = []
# for i in XheightList:
#     i = i.replace("cm","")
#     i = int(i)
#     XheightList1.append(i)
#
# YheightList = list(heightList["2"])



'''
饼形图
int化age列表
ageIntList
'''
# ageIntList = []
# for i in d["2"]:
#     i = i.replace("岁","")
#     ageIntList.append(int(i))
# ageDF = pd.DataFrame(ageIntList,columns=["age"])
# XageList = ['舞象之年..-20',"花信年华21-30",'半老徐娘31-40',"风韵犹存41-.."]
# YageList = []
#
# YageList.append(ageDF[ageDF[ageDF.age>13]<20].count())
# YageList.append(ageDF[ageDF[ageDF.age>19]<30].count())
# YageList.append(ageDF[ageDF[ageDF.age>29]<40].count())
# YageList.append(ageDF[ageDF[ageDF.age>39]<90].count())


'''
现状和城市的散点图
'''

reload(sys)
sys.setdefaultencoding("utf-8")
# Columnar_graph(XheightList1,YheightList,"身").show()

#pie_graph(XageList,YageList,"年龄分段").show()
#
# pie_graph(XmaritalStatusList,YmaritalStatusList,"现况饼形图").show()
# Columnar_graph(clearLocationName1,dogProportion,"地区","占比","未婚占比").show()
# Columnar_graph(clearLocationName1,pingList,"地区","平均身高","平均分高（按地区分组）").show()
# educationList = [0.532,0.667157,0.59961,0.3913,0.69561,0.2436,0.981514225,0.835481,0.610254,0.41526,0.468218,0.48181621,0.4821566,0.412571,0.4598126,0.9365158,0.5814712
#     ,0.2368145,0.3615571,0.75321,0.651641,0.564171,0.512347,0.561684,0.5651653]
incomeList = [5312,4440,4160,3960,4360,2681,12451,5570,4110,2970,3400,3220,2987,3600,
              4320,6821,2405,4152,3660,4890,3520,3102,4040,4120,4546]
# Columnar_graph(clearLocationName1,educationList,"地区","学历指数","学历指数（按地区分组）").show()
Columnar_graph(clearLocationName1,incomeList,"地区","平均收入","平均收入（按地区分组）").show()
for i in clearLocationName1:
    print i




