#_*_coding:utf8_*_

import pymongo
import pandas as pd
import numpy as np
import matplotlib.pylab as plt

client = pymongo.MongoClient('192.168.1.123',27017)
fangdb = client['fangdb']
newfanginfo = fangdb['20171121140104']
df = pd.DataFrame(list(newfanginfo.find()))
df1 = df.loc[:,['EstateArea','RefPrice','AvePrice','HuXing']]

areas = [u'北京',u'上海',u'深圳',u'广州',u'杭州',u'东莞',u'惠州',u'佛山',u'珠海']
areasmeans = []
for i in xrange(0,len(areas)):
    areasdf = df1.loc[df['EstateArea'].isin([areas[i]])]
    areasave = areasdf['RefPrice']*10000/areasdf['HuXing']
    areasmean = areasave.mean()
    areasmeans.append(areasmean)










