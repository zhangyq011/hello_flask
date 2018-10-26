#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask,request,render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "hello word"

@app.route('/query_url')
def query_url():
    return 'query_url' + url_for('query_user')

if __name__=='__main__':
    app.run()




