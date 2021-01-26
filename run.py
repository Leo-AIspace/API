#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, jsonify
from flask_cors import CORS
import function 

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'Hello !!'

@app.route('/post',methods=['POST'])
def Craw():
    result = function.stock()
    return jsonify({'result':str(result)})

if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)
