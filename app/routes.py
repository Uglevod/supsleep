# -*- coding: utf-8 -*-
from app   import app
from app   import mongo
from app   import mpcollection
from flask import request, jsonify


@app.route('/upsl')
def index(): # начальная меню панель 
    return "Hello, World!"

@app.route('/upsl/adday ')
def index(): # хама форма добавления дня
    return "Hello, World!"

@app.route('/upsl/api/adday, methods=['GET', 'POST'] ')
def index(): # сюда json 
    content = request.json
    mongo.ddt.insert_one({'date': content['date'] ,'round': content['round'],'week': content['week'],'up': '-','sleep': '-','nup': content['nup'],'nsleep': content['nsleep']  })
    return flask.jsonify(message="success")

     
    



@app.route('/upsl/liday')
def index():
    return "Hello, World!"

@app.route('/upsl/sutr')
def index(): # ajhvf ryjgrf dhtvz lf форма время дата - редирект на sshow
    return "Hello, World!"

@app.route('/upsl/api/sutr' , methods=['GET', 'POST'] ')
def index(): # сюда json 
    content = request.json
    return "Hello, World!"



@app.route('/upsl/slep')
def index():
    return "Hello, World!"

@app.route('/upsl/api/slep' , methods=['GET', 'POST'] ')
def index(): # сюда json 
    content = request.json
    return "Hello, World!"

@app.route('/upsl/sush')
def index():
    return "Hello, World!"
