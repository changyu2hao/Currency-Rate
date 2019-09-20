import json
from django.http import HttpResponse

import requests

# log in
def get_trans(request):
    number = request.GET.get('number')
    type = request.GET.get('type')
    print(number)
    print(type)

    # get the latest rate from api
    data_first = requests.get(url="https://openexchangerates.org/api/latest.json?app_id=77ccc983deff40dfbf16c75f8cb42fed")

    # calculate the rate and convert it
    pricecny =  round( (float(data_first.json()["rates"]["CNY"])),2)
    pricecanada=round( (float(data_first.json()["rates"]["CAD"])),2)
    price_cad_to_cny=pricecny/pricecanada

    # get the CNY amount
    all_rmb = int(number) * price_cad_to_cny

    # get the USD amount
    priceusd=round( (float(data_first.json()["rates"]["CAD"])),2)
    all_usd=int(number) * (1/priceusd)

    #get the GBP amount
    pricegbp=round((float(data_first.json()["rates"]["GBP"])), 2)
    price_cad_to_gbp=pricegbp/pricecanada

    #get the EUR amount
    priceeur=round((float(data_first.json()["rates"]["EUR"])), 2)
    price_cad_to_eur=priceeur/pricecanada

    #get the JPY amount
    pricejpy=round((float(data_first.json()["rates"]["JPY"])), 2)
    price_cad_to_jpy = pricejpy / pricecanada

    #get the BRL amount
    pricebrl=round((float(data_first.json()["rates"]["BRL"])), 2)
    price_cad_to_brl = pricebrl / pricecanada

    #get the VND amount
    pricevnd = round((float(data_first.json()["rates"]["VND"])), 2)
    price_cad_to_vnd = pricevnd / pricecanada

    pricesgd = round((float(data_first.json()["rates"]["SGD"])), 2)
    price_cad_to_sin = pricesgd/pricecanada


    back = ''
    if type == 'CNY':
        back = all_rmb
    elif type == 'USD':
        back = all_usd
    elif type == 'GBP':
        back =int(number)* price_cad_to_gbp
    elif type == 'EUR':
        back = int(number) * price_cad_to_eur
    elif type =='JPY':
        back=int(number)*price_cad_to_jpy
    elif type=='BRL':
        back = int(number) * price_cad_to_brl
    elif type == 'VND':
        back = int(number) * price_cad_to_vnd
    elif type == 'SGD':
        back = int(number)*price_cad_to_sin
    # print(data_last.json())

    return HttpResponse(json.dumps({"code": 1, "data": back}, ensure_ascii=False))
