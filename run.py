#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: UTF-8 -*-
from flask import Flask, request, jsonify
from flask_cors import CORS
from app import stock


# In[ ]:


app = Flask(__name__)
@app.route('/',methods=['POST'])
def Craw():
    result = stock()
    return(jsonify(result))
if __name__=='__main__':
    app.run()


# In[ ]:




