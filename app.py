from flask import Flask, request, render_template
from datetime import datetime

from processing import call_parkopedia_api, get_feature, get_latitude, get_longitude, get_placeholder, get_average

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["APPLICATION_ROOT"] = "/"

def show_results(lat,lon,radius, sc):
    q = str(lat) + ',' + str(lon)
    add_ph, country = get_placeholder(q)

    nl = gb = ie = fr = de = be = dk = ""
    if country == 'nl':
        nl = "selected"
    elif country == 'gb':
        gb = "selected"
    elif country == 'ie':
        ie = "selected"
    elif country == 'fr':
        fr = "selected"
    elif country == 'de':
        de = "selected"
    elif country == 'be':
        be = "selected"
    elif country == 'dk':
        dk = "selected"

    competitors = call_parkopedia_api(lat, lon, radius)

    mains = ['Interparking','Indigo','Contipark','Apcoa','APCOA','Effia','Goldbeck','NCP','Saba']
    
    operators = []

    rows = ""
    markers = ""

    total_spaces = qpark_spaces = nqpark_spaces = 0
    avg_weekhour = avg_qpark_weekhour = avg_nqpark_weekhour = 0
    avg_weekendhour = avg_qpark_weekendhour = avg_nqpark_weekendhour = 0
    avg_weekday = avg_qpark_weekday = avg_nqpark_weekday = 0
    avg_weekendday = avg_qpark_weekendday = avg_nqpark_weekendday = 0
    count1 = qpark_count1 = nqpark_count1 = 0
    count2 = qpark_count2 = nqpark_count2 = 0
    count3 = qpark_count3 = nqpark_count3 = 0
    count4 = qpark_count4 = nqpark_count4 = 0

    numbering = 1

    try:
        currency = str(competitors['result']['spaces'][0]['priceschema']['currency'])
    except:
        currency = ""

    marker_id = []
    for i in range(len(competitors['result']['spaces'])):
        mark_id = "marker" + str(i)
        marker_id.append(mark_id)

    for i in range(len(competitors['result']['spaces'])):

        if get_feature(competitors,i,'num') != 'null':
            total_spaces += int(get_feature(competitors,i,'num'))
        if competitors['result']['spaces'][i]['cprices']['items'][0]['amount'] > 0:
            avg_weekhour += float(competitors['result']['spaces'][i]['cprices']['items'][0]['amount'])
            count1 += 1
        if competitors['result']['spaces'][i]['cprices']['items'][1]['amount'] > 0:
            avg_weekday += float(competitors['result']['spaces'][i]['cprices']['items'][1]['amount'])
            count2 += 1
        if competitors['result']['spaces'][i]['cprices']['items'][2]['amount'] > 0:
            avg_weekendhour += float(competitors['result']['spaces'][i]['cprices']['items'][2]['amount'])
            count3 += 1
        if competitors['result']['spaces'][i]['cprices']['items'][3]['amount'] > 0:
            avg_weekendday += float(competitors['result']['spaces'][i]['cprices']['items'][3]['amount'])
            count4 += 1
            
        operators.append(str(competitors['result']['spaces'][i]['addresses'][0]))

        if "Q-Park" in str(competitors['result']['spaces'][i]['addresses'][0]):
            icon_function = "highlight_qpark"
            icon_call = "{icon: new L.qparkIcon({number: '" + str(numbering) + "'})}"
            isqpark = 1

            if get_feature(competitors,i,'num') != 'null':
                qpark_spaces += int(get_feature(competitors,i,'num'))
            if competitors['result']['spaces'][i]['cprices']['items'][0]['amount'] > 0:
                avg_qpark_weekhour += float(competitors['result']['spaces'][i]['cprices']['items'][0]['amount'])
                qpark_count1 += 1
            if competitors['result']['spaces'][i]['cprices']['items'][1]['amount'] > 0:
                avg_qpark_weekday += float(competitors['result']['spaces'][i]['cprices']['items'][1]['amount'])
                qpark_count2 += 1
            if competitors['result']['spaces'][i]['cprices']['items'][2]['amount'] > 0:
                avg_qpark_weekendhour += float(competitors['result']['spaces'][i]['cprices']['items'][2]['amount'])
                qpark_count3 += 1
            if competitors['result']['spaces'][i]['cprices']['items'][3]['amount'] > 0:
                avg_qpark_weekendday += float(competitors['result']['spaces'][i]['cprices']['items'][3]['amount'])
                qpark_count4 += 1
        else:
            if any(x in str(competitors['result']['spaces'][i]['addresses'][0]) for x in mains):
                icon_function = "highlight_main"
                icon_call = "{icon: new L.maincompIcon({number: '" + str(numbering) + "'})}"
            else:
                icon_function = "highlight_standard"
                icon_call = "{icon: new L.standardIcon({number: '" + str(numbering) + "'})}"
            isqpark = 0

            if get_feature(competitors,i,'num') != 'null':
                nqpark_spaces += int(get_feature(competitors,i,'num'))
            if competitors['result']['spaces'][i]['cprices']['items'][0]['amount'] > 0:
                avg_nqpark_weekhour += float(competitors['result']['spaces'][i]['cprices']['items'][0]['amount'])
                nqpark_count1 += 1
            if competitors['result']['spaces'][i]['cprices']['items'][1]['amount'] > 0:
                avg_nqpark_weekday += float(competitors['result']['spaces'][i]['cprices']['items'][1]['amount'])
                nqpark_count2 += 1
            if competitors['result']['spaces'][i]['cprices']['items'][2]['amount'] > 0:
                avg_nqpark_weekendhour += float(competitors['result']['spaces'][i]['cprices']['items'][2]['amount'])
                nqpark_count3 += 1
            if competitors['result']['spaces'][i]['cprices']['items'][3]['amount'] > 0:
                avg_nqpark_weekendday += float(competitors['result']['spaces'][i]['cprices']['items'][3]['amount'])
                nqpark_count4 += 1

        prices = []
        curr = []
        for p in range(4):
            price = competitors['result']['spaces'][i]['cprices']['items'][p]['amount']
            if price == -1:
                prices.append('NA')
                curr.append('')
            else:
                prices.append(price)
                curr.append(currency)


        rows += "<tr onclick=\"{func}({idd},{num})\"><td>{num}</td><td>{name}</td><td>{comp}</td><td>{size}</td><td>{distance} m</td><td>{price1} {cur1}</td><td>{price2} {cur2}</td><td>{price3} {cur3}</td><td>{price4} {cur4}</td><td><input type=\"checkbox\" id=\"chck_{idx}\" onclick=\"checkbox({idx},{idd},{isq})\" checked/></td></tr>".format(name=str(competitors['result']['spaces'][i]['title']),\
        comp=str(competitors['result']['spaces'][i]['addresses'][0]),\
        size=get_feature(competitors,i,'num'),idx=i,func=icon_function,isq=isqpark,num=numbering,\
        distance=str(competitors['result']['spaces'][i]['distance']),\
        idd=marker_id[i], price1=prices[0], price2=prices[1],price3=prices[2], price4=prices[3],\
        cur1=curr[0], cur2=curr[1], cur3=curr[2], cur4=curr[3])

        markers += "var {idd} = L.marker([{latitude}, {longitude}],{icon}); {idd}.addTo(map).bindPopup('{num}. {op}<br>{name}');".format(latitude=str(competitors['result']['spaces'][i]['lat']),\
        longitude=str(competitors['result']['spaces'][i]['lng']),\
        name=str(competitors['result']['spaces'][i]['title']).replace("'",''),\
        idd=marker_id[i],num=numbering,\
        op=str(competitors['result']['spaces'][i]['addresses'][0]).replace("'",''),\
        icon=icon_call)

        numbering += 1


    avg_weekhour = get_average(avg_weekhour,count1)
    avg_weekday = get_average(avg_weekday,count2)
    avg_weekendhour = get_average(avg_weekendhour,count3)
    avg_weekendday = get_average(avg_weekendday,count4)
    avg_qpark_weekhour = get_average(avg_qpark_weekhour,qpark_count1)
    avg_qpark_weekday = get_average(avg_qpark_weekday,qpark_count2)
    avg_qpark_weekendhour = get_average(avg_qpark_weekendhour,qpark_count3)
    avg_qpark_weekendday = get_average(avg_qpark_weekendday,qpark_count4)
    avg_nqpark_weekhour = get_average(avg_nqpark_weekhour,nqpark_count1)
    avg_nqpark_weekday = get_average(avg_nqpark_weekday,nqpark_count2)
    avg_nqpark_weekendhour = get_average(avg_nqpark_weekendhour,nqpark_count3)
    avg_nqpark_weekendday = get_average(avg_nqpark_weekendday,nqpark_count4)

    if qpark_spaces > 0 or nqpark_spaces > 0:
        qperc = round((qpark_spaces / (qpark_spaces + nqpark_spaces) * 100),1)
        nperc = round((100 - qperc),1)
    else:
        qperc = nperc = 0

    now = datetime.now()
    now_form = now.strftime("%Y%m%d-%H%M%S")
    
    operators = list(dict.fromkeys(operators))
    operators_selector = ""
    for op in operators:
        if "Q-Park" in op:
            operators_selector += '<option class="qp" value="' + op + '">' + op + '</option>'
        elif any(x in op for x in mains):
            operators_selector += '<option class="main" value="' + op + '">' + op + '</option>'
        else:
            operators_selector += '<option value="' + op + '">' + op + '</option>'
    
    if sc:
        return render_template('showcase.html', latt=str(lat), lonn=str(lon), markers=markers,cur=currency,now=now_form,\
        rows=rows,spaces=total_spaces,day=avg_weekday,day_we=avg_weekendday,hour=avg_weekhour,hour_we=avg_weekendhour,\
        spaces2=qpark_spaces,spaces3=nqpark_spaces,day2=avg_qpark_weekday,day3=avg_nqpark_weekday,day2_we=avg_qpark_weekendday,day3_we=avg_nqpark_weekendday,hour2=avg_qpark_weekhour,\
        hour3=avg_nqpark_weekhour,hour2_we=avg_qpark_weekendhour,hour3_we=avg_nqpark_weekendhour,qperc=qperc, nperc=nperc, count1=count1,count2=count2,count3=count3,count4=count4,\
        count21=qpark_count1,count22=qpark_count2,count23=qpark_count3,count24=qpark_count4,count31=nqpark_count1,count32=nqpark_count2,count33=nqpark_count3,count34=nqpark_count4, op_options=operators_selector)
    else:
        return render_template('results.html', latt=str(lat), lonn=str(lon), markers=markers,cur=currency,now=now_form,ph=add_ph,nlph=nl,beph=be,gbph=gb,dkph=dk,deph=de,frph=fr,ieph=ie,\
        rows=rows,spaces=total_spaces,day=avg_weekday,day_we=avg_weekendday,hour=avg_weekhour,hour_we=avg_weekendhour,\
        spaces2=qpark_spaces,spaces3=nqpark_spaces,day2=avg_qpark_weekday,day3=avg_nqpark_weekday,day2_we=avg_qpark_weekendday,day3_we=avg_nqpark_weekendday,hour2=avg_qpark_weekhour,\
        hour3=avg_nqpark_weekhour,hour2_we=avg_qpark_weekendhour,hour3_we=avg_nqpark_weekendhour,qperc=qperc, nperc=nperc, count1=count1,count2=count2,count3=count3,count4=count4,\
        count21=qpark_count1,count22=qpark_count2,count23=qpark_count3,count24=qpark_count4,count31=nqpark_count1,count32=nqpark_count2,count33=nqpark_count3,count34=nqpark_count4, op_options=operators_selector)
    

@app.route("/", methods=["GET", "POST"])
def adder_page():
    try:
        errors = ""
        if request.method == "POST":
            lat = None
            lon = None
            radius = None
            try:
                lat = float(request.form["lat"])
            except:
                try:
                    lat = float(get_latitude(request.form["add"],request.form["country"]))
                except:
                    errors += "<p>Incorrect latitude or address</p>\n"
            try:
                lon = float(request.form["lon"])
            except:
                try:
                    lon = float(get_longitude(request.form["add"],request.form["country"]))
                except:
                    errors += "<p>Incorrect longitude or address</p>\n"
            try:
                radius = int(request.form["radius"])
            except:
                errors += "<p>{!r} is not a number.</p>\n".format(request.form["radius"])

            if lat is not None and lon is not None and radius is not None:
                try:
                    
                    return show_results(lat,lon,radius, False)
                
                except Exception as e:
                    errors += "<p>{!r}</p>\n".format(e)

        return render_template('input.html',errors=errors)

    except Exception as e:
        print(e)


@app.route("/showcase", methods=["GET", "POST"])
def showcase():
    if request.method == "GET":
        lat = None
        lon = None
        radius = None
    
        lat = float(request.args.get('lat'))
        lon = float(request.args.get('lon'))
        radius = int(request.args.get('r'))
    
        if lat is not None and lon is not None and radius is not None:
                
            return show_results(lat, lon, radius, True)
    
@app.route("/test")
def test():      
  
    try:
        import pyodbc
        import pandas as pd
    
        conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=qpara-qpark304;'
                          'Database=DWH;'
                          'Trusted_Connection=yes;'
                         )
        
        testt = pd.read_sql_query('SELECT [PF_SearchName] FROM [DWH].[DIM].[DIM_ParkingFacility]',conn)
        
        toprint = ""
        for i in testt:
            toprint += '<p>' + str(testt[i]) + '</p>'
            
        return toprint
    
    except Exception as e:
        return e
