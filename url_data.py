
import requests
import json
import pprint

class Url_data: 
    def __init__(self, *args, **kwargs):
        self.url = requests.get('https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1')
        self.json_data=self.url.json()
        

    def obtener_datos_bd(self): 
        #self.json_data['items'][0]['commonName'] 
        for data in self.json_data: 
            query = "insert into players values {}".format(data)
            print(query)

fifa = Url_data()
fifa.obtener_datos_bd()