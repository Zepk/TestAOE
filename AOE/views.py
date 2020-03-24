from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import requests
import json


def index(request):
    a = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations')
    datos = a.json()
    template = loader.get_template('AOE/index.html')

    for i in datos['civilizations']:
        lista_unidades = []
        lista_techs = []
        civ_bonus_string = ''
        for unit in i['unique_unit']:
            req = requests.get(unit)
            req = req.json()
            lista_unidades.append(req['name'])
        for tech in i['unique_tech']:
            req = requests.get(tech)
            req = req.json()
            lista_techs.append(req['name'])
        for bonus in i['civilization_bonus']:
            civ_bonus_string = '{}, {}'.format(civ_bonus_string, bonus)

        i.update({'civilization_bonus': civ_bonus_string[2:-1]})
        i.update({'unique_unit_list': lista_unidades})
        i.update({'unique_tech_list': lista_techs})


    context = {
        'datos': datos,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the polls index.")

def unitdetail(request):

    template = loader.get_template('AOE/unitdetail.html')




    context = {
        'datos': datos,
    }
    return HttpResponse(template.render(context, request))
