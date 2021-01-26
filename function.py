#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import requests as req
from io import StringIO


# In[2]:


def stock():
    html = req.get('https://www.twse.com.tw/fund/BFI82U?response=html&dayDate=&weekDate=&monthDate=&type=day')
    html.encoding='utf-8'
    table = pd.read_html(StringIO(html.text),header=0)
    df = table[0]
    df.drop(labels=df.columns[1:-1],axis=1,inplace=True)
    df.drop(labels=0,axis=0,inplace=True)
    df['110年01月26日 三大法人買賣金額統計表.3'] = df['110年01月26日 三大法人買賣金額統計表.3'].apply(
    lambda x : '{:.2f}億'.format(int(x)/100000000))
    Date = list(df.columns)[0]
    a = df[:].values.reshape(-1)
    
#     return(Date,str(a[0]),str(a[1]),str(a[2]),str(a[3]),str(a[4]),str(a[5]))
#     return(str(Date),f'{a[0]}: {a[1]}',f'{a[2]}: {a[3]}',f'{a[4]}: {a[5]}',f'{a[6]}: {a[7]}',
#            f'{a[8]}: {a[9]}',f'{a[10]}: {a[11]}')
    return(Date)


# In[ ]:




