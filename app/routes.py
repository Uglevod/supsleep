# -*- coding: utf-8 -*-
from app   import app
from app   import mongo
#from app import base

#from app   import mpcollection
from flask import request, jsonify, url_for
from flask import render_template
import datetime
import json 
import pymongo




base = ""

@app.route('/')
def indexi(): # начальная меню панель 
    base = request.base_url
    print(base)
    return render_template('index.html', base=base )
    


@app.route('/upsl')
def index(): # начальная меню панель 
    #base = request.base_url
    #print(base)
    

    return render_template('index.html', base=base )


@app.route('/upsl/adday')
def adday(): # хама форма добавления дня
    x    = datetime.datetime.now()
    date = x.strftime("%d.%m.%y")
    time = x.strftime("%H.%M") 
    
    #base = request.base_url
    #print(base)
    host = base+url_for('api_adday')
    gthost = base+url_for('api_gtlist')
    return render_template('addday.html', date=date, time=time, host=host,gthost=gthost)

@app.route('/upsl/api/adday', methods=[ 'POST'] )
def api_adday(): # сюда json 
    content = request.get_json(force=True)
    #content = request.get_json(silent=True)
    print("---",content,"---")
    #mongo.db.ddt.insert_one({"round": content['round'],"week": content['week'],"date": content['date'] ,"wkd": content['wkd'] ,"up": '-',"sleep": '-',"nup": content['nup'],"nsp": content['nsp']  })
    #mongo.db.ddt.insert_one({'date': "22222" ,'round': 3,'week': 23,'up': '-','sleep': '-','nup': '3333','nsleep': '7777'  })
    

    mongo.db.ddt.find_and_modify(query={'date':content['date']}, update={"$set": { "round": content['round'],"week": content['week'],"date": content['date'] ,"wkd": content['wkd'] ,"nup": content['nup'],"nsp": content['nsp'] }}, upsert=True, full_response= True)
  



    response = app.response_class(
            response=json.dumps({"status":"ok","day":"added"}),
            status=200,
            mimetype='application/json'

    )
    return response

@app.route('/upsl/api/gtlist', methods=[ 'GET','POST'] )
def api_gtlist(): # сюда json 
    
    ans=[]
    for oo in mongo.db.ddt.find().sort([("date", pymongo.ASCENDING)]).limit(30):
        print("/////",oo.pop("_id", None),"/////")
        ans.append(oo)

    print("5555555555",ans,"55555555555555")

    
    return json.dumps(ans)



    #return flask.jsonify(message="success")

#--------------------------- UTRO--------------------------------
 
@app.route('/upsl/sutr')
def sutro(): # ajhvf ryjgrf dhtvz lf форма время дата - редирект на sshow
    x    = datetime.datetime.now()
    date = x.strftime("%d.%m.%y")
    time = x.strftime("%H.%M") 
    
    host = base+url_for('api_sutro')
    print("upr",base,"upr")
     
    return render_template('sutr.html', date=date, time=time, host=host )


@app.route('/upsl/api/sutr' , methods=['GET', 'POST'] )
def api_sutro(): # сюда json 
    content = request.get_json(force=True)
    #content = request.get_json(silent=True)
    print("---",content,"---")
    mongo.db.ddt.find_and_modify(query={'date':content['upd']}, update={"$set": {'up': content['upt']}}, upsert=True, full_response= True)
  

    #mongo.db.ddt.insert_one({"round": content['round'],"week": content['week'],"date": content['date'] ,"wkd": content['wkd'] ,"up": '-',"sleep": '-',"nup": content['nup'],"nsp": content['nsp']  })
    #mongo.db.ddt.insert_one({'date': "22222" ,'round': 3,'week': 23,'up': '-','sleep': '-','nup': '3333','nsleep': '7777'  })
    
    response = app.response_class(
            response=json.dumps({"status":"ok","sutr":"added"}),
            status=200,
            mimetype='application/json'

    )
    return response
 

#--------------------------- SLEEP --------------------------------
 

@app.route('/upsl/sleep')
def sleep():
    x    = datetime.datetime.now()
    date = x.strftime("%d.%m.%y")
    time = x.strftime("%H.%M") 
    
    host = base+url_for('api_sleep')
    print("slp",base,"slp")
     
    return render_template('slep.html', date=date, time=time, host=host )

@app.route('/upsl/api/sleep' , methods=['GET', 'POST'] )
def api_sleep(): # сюда json 

    content = request.get_json(force=True)
    #content = request.get_json(silent=True)
    print("---",content,"---")
    mongo.db.ddt.find_and_modify(query={'date':content['date']}, update={"$set": {'sleep': content['sleep']}}, upsert=True, full_response= True)
  

    #mongo.db.ddt.insert_one({"round": content['round'],"week": content['week'],"date": content['date'] ,"wkd": content['wkd'] ,"up": '-',"sleep": '-',"nup": content['nup'],"nsp": content['nsp']  })
    #mongo.db.ddt.insert_one({'date': "22222" ,'round': 3,'week': 23,'up': '-','sleep': '-','nup': '3333','nsleep': '7777'  })
    
    response = app.response_class(
            response=json.dumps({"status":"ok","sleep":"added"}),
            status=200,
            mimetype='application/json'

    )
    return response

#--------------------------- SHOW --------------------------------

@app.route('/upsl/sush')
def supslsh():

    #host = base+url_for('supslsh')
    host = base+url_for('api_gtlist') 
    print("slp",base,"slp")
     
    return render_template('supslsh.html',   gshost=host )

@app.route('/upsl/api/sush')
def supslsh_api():

    host = base+url_for('api_show')

    print("slp",base,"slp")
     
    return render_template('supslsh.html', date=date, time=time, gshost=host )



# Хотите лечь наньше 
# Что помоглао лечь вовремя благодаяо чему 
# cgfnm nfr cgfnm спать так спать 
# vekmnb .pt  мульти юзер на малое число пользователей
# Почему ложитесь поздно - что помешало - что можно предусмотреть 
# Пункты - на стартовой
#htubcnhfwbz регистрация по емылу и парорлю
# rак спалось - какой был сон 
# что для улучшения сна - для просыпания сделать  
# сон по среди дня

# дела перед сном - чеклист - пока все не сделаны - кнопка сна не активна

# yfcnhjqrf Настройка действий с утра

# bcnjhbz история блог проектов 
# gj;llth;rf поддерка и мое восприятие поддержки 


# старт проекта - стадия - насалось закончил - результат - план 

# [hjyj Хроно с разными типами события
# Завтрах обед - ужин -- 5 чаепитий - утро подьем - ко сну - 5 чтений 
# ghjuhfvvbyu ghjuekrf программинг прогулка но вое 
# вывод - nfkbwf ltjhtdj



#№№ телега рега
#1 выписка - маркир - сорт - наборы ... 
#2 автоплан 
#3 играть план 
#4 послеплан 

# pfhtkbpbnm ctqxfc зарелизить сейчас про сон и юзать месяц 

# згрузить на гит
# загруз на жино - установка без окружения - настройка нг supsl.pypride.ru 
