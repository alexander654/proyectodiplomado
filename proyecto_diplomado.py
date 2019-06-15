import operator
from flask import Flask, request
from bson.json_util import dumps
from pymongo import MongoClient
import pandas as pd
import pymongo

#conexion con la db
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['proyecto']
mycol = mydb['export']

datos_mosquitos = pd.DataFrame(list(mycol.find()))

#print(datos_mosquitos)
#print('1. ¿Cual es la mayor cantidad de mosquitos vista?')
#print('La mayor cantidad de mosquitos es %s' % (datos_mosquitos.loc[:,'Specimens collected'].max()))
def max_mosquitoes():
    return str(datos_mosquitos.loc[:,'Specimens collected'].max())
#print('2. ¿Que tipo de mosquitos existe?')
#lista=datos_mosquitos.loc[:,'Species'].tolist()
#lista = list(dict.fromkeys(lista))
#print(lista)
def mosquitoes_type():
    lista=datos_mosquitos.loc[:,'Species'].tolist()
    lista = list(dict.fromkeys(lista))
    return str(lista)
#print('3. ¿Cual es el tipo de trampa que captura mas mosquitos?')
#dic=dict()
#for index, row in datos_mosquitos.iterrows():
#    key=row[2]
#    if key in dic:
#        dic[key]+=row[6]
#    else:
#        dic[key]=row[6]
#value=max(dic.items(), key=operator.itemgetter(1))[0]
#print('Trampa %s: mosquitos %s' % (value, dic[value]))
def best_trap():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=row[13]
        if key in dic:
            dic[key]+=row[17]
        else:
            dic[key]=row[17]
    value=max(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(trap=value,mosquitoes=dic[value])
    return str(result)
#print('4. ¿Cual es la especie mas grande de mosquitos?')
#dic=dict()
#for index, row in datos_mosquitos.iterrows():
#    key=row[8]
#    if key in dic:
#        dic[key]+=row[6]
#    else:
#        dic[key]=row[6]
#value=max(dic.items(), key=operator.itemgetter(1))[0]
#print('Especie %s: mosquitos %s' % (value, dic[value]))
def great_mosquito_type():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=row[7]
        if key in dic:
            dic[key]+=row[17]
        else:
            dic[key]=row[17]
    value=max(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(specie=value,mosquitoes=dic[value])
    return str(result)
# print('5. ¿Cual es la especie mas pequeña de mosquitos?')
# dic=dict()
# for index, row in datos_mosquitos.iterrows():
#     key=row[8]
#     if key in dic:
#         dic[key]+=row[6]
#     else:
#         dic[key]=row[6]
# value=min(dic.items(), key=operator.itemgetter(1))[0]
# print('Especie %s: mosquitos %s' % (value, dic[value]))
def less_mosquito_type():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=row[7]
        if key in dic:
            dic[key]+=row[17]
        else:
            dic[key]=row[17]
    value=min(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(specie=value,mosquitoes=dic[value])
    return str(result)
# print('6. ¿Año y semana con mas mosquitos?')
# dic=dict()
# for index, row in datos_mosquitos.iterrows():
#     key=(index,row[0])
#     if key in dic:
#         dic[key]+=row[6]
#     else:
#         dic[key]=row[6]
# value=max(dic.items(), key=operator.itemgetter(1))[0]
# print('Es: %s con %s' % (value, dic[value]))
def best_season_trap():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=(index,row[3])
        if key in dic:
            dic[key]+=row[17]
        else:
            dic[key]=row[17]
    value=max(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(date=value,mosquitoes=dic[value])
    return str(result)
# print('7. ¿Cual es el zip code donde aparecen mas mosquitos?')
# dic=dict()
# for index, row in datos_mosquitos.iterrows():
#     key=row[14]
#     if key in dic:
#         dic[key]+=row[6]
#     else:
#         dic[key]=row[6]
# value=max(dic.items(), key=operator.itemgetter(1))[0]
# print('Zip code: %s con %s mosquitos' % (value, dic[value]))
def zip_code_more_mosquitoes():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=row[9]
        if key in dic:
            dic[key]+=row[17]
        else:
            dic[key]=row[17]
    value=max(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(zip=value,mosquitoes=dic[value])
    return str(result)
# print('8. ¿Zip codes mas evaluados?')
# dic=dict()
# for index, row in datos_mosquitos.iterrows():
#     key=row[14]
#     if key in dic:
#         dic[key]+=1
#     else:
#         dic[key]=1
# value=max(dic.items(), key=operator.itemgetter(1))[0]
# print('Zip code: %s con %s apariciones' % (value, dic[value]))
def most_evaluated_zip():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=row[9]
        if key in dic:
            dic[key]+=1
        else:
            dic[key]=1
    value=max(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(zip=value,shows=dic[value])
    return str(result)
# print('9. ¿Zip codes menos evaluados?')
# dic=dict()
# for index, row in datos_mosquitos.iterrows():
#     key=row[14]
#     if key in dic:
#         dic[key]+=1
#     else:
#         dic[key]=1
# value=min(dic.items(), key=operator.itemgetter(1))[0]
# print('Zip code: %s con %s apariciones' % (value, dic[value]))
def less_evaluated_zip():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=row[9]
        if key in dic:
            dic[key]+=1
        else:
            dic[key]=1
    value=min(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(zip=value,shows=dic[value])
    return str(result)
# print('10. ¿Cual es el tipo de trampa que captura menos mosquitos?')
# dic=dict()
# for index, row in datos_mosquitos.iterrows():
#     key=row[4]
#     if key in dic:
#         dic[key]+=row[6]
#     else:
#         dic[key]=row[6]
# value=min(dic.items(), key=operator.itemgetter(1))[0]
# print('Trampa %s: mosquitos %s' % (value, dic[value]))
def worst_mosquito_trap():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=row[2]
        if key in dic:
            dic[key]+=row[17]
        else:
            dic[key]=row[17]
    value=min(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(trap=value,mosquitoes=dic[value])
    return str(result)   
# print('11. ¿En que fecha aparecio la mayor cantidad de mosquitos?')
# dic=dict()
# for index, row in datos_mosquitos.iterrows():
#     key=row[5]
#     if key in dic:
#         dic[key]+=row[6]
#     else:
#         dic[key]=row[6]
# value=max(dic.items(), key=operator.itemgetter(1))[0]
# print('Fecha %s: mosquitos %s' % (value, dic[value]))
def best_trap_date():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=row[3]
        if key in dic:
            dic[key]+=row[17]
        else:
            dic[key]=row[17]
    value=max(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(date=value,mosquitoes=dic[value])
    return str(result)
# print('12. ¿En que fecha aparecio la menor cantidad de mosquitos?')
# dic=dict()
# for index, row in datos_mosquitos.iterrows():
#     key=row[5]
#     if key in dic:
#         dic[key]+=row[6]
#     else:
#         dic[key]=row[6]
# value=min(dic.items(), key=operator.itemgetter(1))[0]
# print('Fecha %s: mosquitos %s' % (value, dic[value]))
def worst_trap_date():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=row[3]
        if key in dic:
            dic[key]+=row[17]
        else:
            dic[key]=row[17]
    value=min(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(date=value,mosquitoes=dic[value])
    return str(result)
# print('13. ¿Año y semana con menos mosquitos?')
# dic=dict()
# for index, row in datos_mosquitos.iterrows():
#     key=(index,row[0])
#     if key in dic:
#         dic[key]+=row[6]
#     else:
#         dic[key]=row[6]
# value=min(dic.items(), key=operator.itemgetter(1))[0]
# print('Es: %s con %s' % (value, dic[value]))
def date_less_mosquito():
    dic=dict()
    for index, row in datos_mosquitos.iterrows():
        key=(index,row[3])
        if key in dic:
            dic[key]+=row[17]
        else:
            dic[key]=row[17]
    value=min(dic.items(), key=operator.itemgetter(1))[0]
    result=dict(date=value,mosquitoes=dic[value])
    return str(result)

def toJson(value):
    return dumps(value)

#base endpoint
base_url='mosquito'
#construccion del webservice
app = Flask(__name__)

#max mosquitoes
@app.route('/{}'.format(base_url), methods=['GET'])
def index():
    return toJson(max_mosquitoes())

#mosquitoes types
@app.route('/{}/types'.format(base_url), methods=['GET'])
def mosquito_types():
    return toJson(mosquitoes_type())

#best trap mosquitoes
@app.route('/{}/best_trap'.format(base_url), methods=['GET'])
def best_trap_mosquito():
    return toJson(best_trap())

#mosquitoes types great
@app.route('/{}/types_great'.format(base_url), methods=['GET'])
def type_mosquito_great():
    return toJson(great_mosquito_type())

#mosquitoes types less
@app.route('/{}/types_less'.format(base_url), methods=['GET'])
def type_mosquito_less():
    return toJson(less_mosquito_type())

#mosquitoes trap best season
@app.route('/{}/trap_best'.format(base_url), methods=['GET'])
def season_trap_best():
    return toJson(best_season_trap())

#zip more mosquitoes
@app.route('/{}/zip_codes'.format(base_url), methods=['GET'])
def more_mosquitoes_zip_codes():
    return toJson(zip_code_more_mosquitoes())

#zip most evaluated
@app.route('/{}/zip_codes_frequent'.format(base_url), methods=['GET'])
def zip_most_evaluated():
    return toJson(most_evaluated_zip())

#zip less evaluated
@app.route('/{}/zip_codes_less_frequent'.format(base_url), methods=['GET'])
def less_zip_evaluated():
    return toJson(less_evaluated_zip())

#less effective trap
@app.route('/{}/trap_less_effective'.format(base_url), methods=['GET'])
def less_effective_trap():
    return toJson(worst_mosquito_trap())

#most effective trap date
@app.route('/{}/date_best'.format(base_url), methods=['GET'])
def effective_trap_date():
    return toJson(best_trap_date())

#less effective trap date
@app.route('/{}/date_worst'.format(base_url), methods=['GET'])
def trap_date_worst():
    return toJson(worst_trap_date())

#date less mosquitos
@app.route('/{}/date_less'.format(base_url), methods=['GET'])
def less_mosquito_date():
    return toJson(date_less_mosquito())

if __name__ == '__main__':
    app.run(debug=True)