
# -*- coding: utf-8 -*-

import json
import requests
import time
from datetime import datetime
import tweepy as tp
from keys import *

# http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/4970/days/15?token=57d6b58e8a5c3f87bb90d52a76f05b3d
# logando na conta api twitter:
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)


def pegadados():
    req = requests.get(
        'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/4970/days/15?token=57d6b58e8a5c3f87bb90d52a76f05b3d')
    res = json.loads(req.text)
    data = res.get("data")
    hoje = data[0]
    amanha = data[1]
    dia = amanha.get("date")

    date = hoje.get("date")
    resumo = hoje.get("text_icon").get("text").get("phrase").get("reduced")
    tempMin = hoje.get("temperature").get("min")
    tempMax = hoje.get("temperature").get("max")
    chuvaProb = hoje.get("rain").get("probability")
    chuvaMm = hoje.get("rain").get("precipitation")
    ventoMedio = hoje.get("wind").get("velocity_avg")
    umidadeMin = hoje.get("humidity").get("min")
    umidadeMax = hoje.get("humidity").get("max")
    sunrise = hoje.get("sun").get("sunrise")
    sunset = hoje.get("sun").get("sunset")
    # print('aaaaaa')
    # for key in res.keys():
    #    print(key)
    chuvaEmoticon = u'\U00002614'
    solEmoticon = u'\U00002600'
    # print('-------------------------------------')
    # print(dia)
    # print('-------------------------------------')
    # print(
    #    f'Previsao do tempo hoje ({date}) em Joinville\n\n{resumo}\n\nTemperatura: min {tempMin}°C max {tempMax}°C\nChance de chuva: {chuvaProb}% ({chuvaMm}mm)\nVento vel. média: {ventoMedio}km/h\nUmidade: min {umidadeMin}% max {umidadeMax}%\nSol: {sunrise} - {sunset}')
    api.update_status('Previsão do tempo hoje ('+str(date)+') em Joinville\n\n'+resumo+'\n\nTemperatura: min '+str(tempMin)+'°C max '+str(tempMax)+'°C\nChance de chuva: ' +
                      str(chuvaProb)+'% '+chuvaEmoticon + ' ('+str(chuvaMm)+'mm)\nVento vel. média: '+str(ventoMedio)+'km/h\nUmidade: min '+str(umidadeMin)+'% max '+str(umidadeMax)+'%\nSol: '+str(sunrise)+' ' + solEmoticon+' ' + str(sunset))
    print("tweet enviado")


pegadados()
