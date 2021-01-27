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
    df[df.columns[-1]] = df[df.columns[-1]].apply(
    lambda x : '{:.2f}億'.format(int(x)/100000000))
    Date = list(df.columns)[0]
    a = df[:].values
    content = ""
    content += f"{Date}\n{str(a[0])}\n{str(a[1])}\n{str(a[2])}\n{str(a[3])}\n{str(a[4])}\n{str(a[5])}"
    return content

# In[ ]:




