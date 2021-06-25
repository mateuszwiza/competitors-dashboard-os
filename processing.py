import random
import requests
import json
import pandas as pd
import datetime
from datetime import date

def get_feature(json, i, name):
    try:
        return str(json['result']['spaces'][i][name])
    except:
        return "null"

def get_price1(outcome, i):
    try:
        output = ""
        for k in range(len((outcome['result']['spaces'][i]['priceschema']['prices'][0]['costs']))):
            if outcome['result']['spaces'][i]['priceschema']['prices'][0]['costs'][k]['dur'] == '60':
                output = str(outcome['result']['spaces'][i]['priceschema']['prices'][0]['costs'][k]['amount'])
                break
        if output == "":
            time = float(outcome['result']['spaces'][i]['priceschema']['prices'][0]['costs'][0]['dur'])
            if time == 1000026:
                time = 1440
            if time == 1000003:
                output = "Flat:" + str(outcome['result']['spaces'][i]['priceschema']['prices'][0]['costs'][0]['amount'])
            else:
                amount = float(outcome['result']['spaces'][i]['priceschema']['prices'][0]['costs'][0]['amount'])
                output = round((amount * (60/time)),2)

            return str(output)
        else:
            return str(output)

    except:
        return 'null'

def get_avgprice(outcome, i):
    try:
        output = 0
        count = 0
        for j in range(len((outcome['result']['spaces'][i]['priceschema']['prices']))):
            for k in range(len((outcome['result']['spaces'][i]['priceschema']['prices'][j]['costs']))):
                time = float(outcome['result']['spaces'][i]['priceschema']['prices'][j]['costs'][k]['dur'])
                amount = float(outcome['result']['spaces'][i]['priceschema']['prices'][j]['costs'][k]['amount'])
                if time == 1000026:
                    time = 1440
                if time == 1000003:
                    output += amount
                else:
                    output += amount * (60/time)
                    count += 1
        return str(round(output/count,2))


    except:
        return "null"

def generate_csv(competitors):
    data = []

    for i in range(len(competitors['result']['spaces'])):
        row = []
        row.append(competitors['result']['spaces'][i]['title'])
        row.append(competitors['result']['spaces'][i]['addresses'][0])
        row.append(get_feature(competitors,i,'num'))
        row.append(competitors['result']['spaces'][i]['distance'])
        row.append(competitors['result']['spaces'][i]['cprices']['items'][0]['amount'])
        row.append(competitors['result']['spaces'][i]['cprices']['items'][1]['amount'])
        row.append(competitors['result']['spaces'][i]['cprices']['items'][2]['amount'])
        row.append(competitors['result']['spaces'][i]['cprices']['items'][3]['amount'])

        data.append(row)

    column_names = ["Name", "Operator", "Spaces","Distance","Weekhour price","Weekday price","Weekendhour price","Weekendday price"]
    df = pd.DataFrame(data, columns = column_names)

    df.to_excel("static/export.xlsx", index=False)
    df.to_csv("static/export.csv", index=False)

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def get_dates():
    d = date.today()
    next_monday = str(next_weekday(d, 0).strftime('%Y%m%d'))
    next_saturday = str(next_weekday(d, 5).strftime('%Y%m%d'))
    dates = next_monday + '1200-' + next_monday + '1300,' + next_monday + '0100-'+\
            next_monday + '2300,' + next_saturday + '1200-' + next_saturday + '1300,' +\
            next_saturday + '0100-'+ next_saturday + '2300'
    return dates

def get_token():
    url = 'https://qpark.parkopedia.com/api/tokens/'
    headers = {"Content-Type": "application/json"}
    payload = {"client_id": "", "client_secret": "", "grant_type": "client_credentials"}

    req = requests.post(url=url, headers=headers, json=payload)
    token = json.loads(req.content)
    return token

def call_parkopedia_api(lat, lng, radius):
    url = 'https://qpark.parkopedia.com/api/search'
    uid = int(random.random()*25)
    dates = get_dates()
    params = {"cid": "qpark-bcab0", "apiver": "31", "uid": str(uid), "lat": str(lat), "lng": str(lng), "radius": str(radius), "dates": dates, "typeids":"4"}
    token = get_token()
    auth = str(token['token_type'])+ ' ' + str(token['access_token'])
    headers = {"Authorization": auth}

    req = requests.get(url=url, params=params, headers=headers)
    response = json.loads(req.content)
    generate_csv(response)
    return response

def get_names(lat, lon, radius):
    outcome = call_parkopedia_api(lat, lon, radius)

    params = []

    count = 0
    if outcome['status'] == 'ERROR':
        params.append(outcome['error'])
    else:
        for i in range(len(outcome['result']['spaces'])):
            params.append(outcome['result']['spaces'][i]['title'])
            count += 1

    return params


def geocoding_api(inp,country):
    url = 'https://api.opencagedata.com/geocode/v1/json'
    auth = ''
    params = {"q": inp, "key": auth, "limit": 1, "countrycode":country}


    req = requests.get(url=url, params=params)
    response = json.loads(req.content)
    return response



def get_latitude(inp,country):
    outcome = geocoding_api(inp,country)
    return outcome['results'][0]['geometry']['lat']

def get_longitude(inp,country):
    outcome = geocoding_api(inp,country)
    return outcome['results'][0]['geometry']['lng']

def get_placeholder(inp):
    url = 'https://api.opencagedata.com/geocode/v1/json'
    auth = ''
    params = {"q": inp, "key": auth, "limit": 1}
    req = requests.get(url=url, params=params)
    response = json.loads(req.content)
    placeholder = response['results'][0]['formatted']
    country = response['results'][0]['components']['country_code']
    return placeholder, country

def get_average(total,count):
    if count > 0:
        return round(total/count,2)
    else:
        return 0
