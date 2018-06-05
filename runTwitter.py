import http.client
import string
from myMongo import MyMongo
import datetime
import pprint
import twitter
import json

conn = http.client.HTTPConnection("192.168.2.199")
conn.request("GET", "/index.htm")
r1 = conn.getresponse()
print(r1.status, r1.reason)
if ( r1.status == 200 ):
    data1 = r1.read()  # This will return entire content.
    print(data1)
    data = str(data1).replace("b'",'').replace("'",'')
    print(data);
    data2 = data.split(',')
    print(data2[3])
    m = MyMongo("meteorologia")
    data = {"humidade":data2[0],"data_hora": datetime.datetime.now(),"temperatura":data2[1],"unidade_humidade":data2[2],"estado":data2[3]}
    _id = m.add("situacao",data)
    print(_id)
    a = m.get_item("situacao",{"_id":_id})
    pprint.pprint(a)
    with open("/home/carlos/Python/arduino/meteorologia/keys.json","r") as arquivo:
        data = json.load(arquivo)
        # print(data["consumer_key"])
    api = twitter.Api(consumer_key=data["consumer_key"],
                      consumer_secret=data["consumer_secret"],
                      access_token_key=data["access_token_key"],
                      access_token_secret=data["access_token_secret"])
    status = api.PostUpdate('Tempo no pé da serra, SJP, Saltinho da malhada, humidade:' + data2[0] + ', temperatura: ' + data2[1] + ', ' + data2[3] + '. Fonte: Arduino Uno + Python #arduino #Iot #python')





    # b = m.get_itens('situacao',{})
    # for c in b:
    #     pprint.pprint(c)
