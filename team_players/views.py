from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse, response
from rest_framework.response import Response
from .models import PlayersRequest,TeamsRequest
from .serializers import PlayersRequestSerializers,TeamRequestSerializers
import requests

# class TeamsRequestViewSet(viewsets.ModelViewSet):
#     serializer_class = TeamsRequestSerializers
#     queryset = TeamsRequest.objects.all()


class TeamRequestViewSet(viewsets.ModelViewSet):
    
    serializer_class = TeamRequestSerializers
    queryset = TeamsRequest.objects.all()
    
    def create(self,request,*args, **kwargs):
        datos = request.data
        #datos['page']
        #json_data['items'][0]['club']['name']
        url = requests.get('https://www.easports.com/fifa/ultimate-team/api/fut/item?page={}'.format(datos['page']))
        json_data=url.json()
        club = datos['team'].upper()
        players = []
        data_respuesta={}
        for items in json_data['items']: 
            item_club = items['club']['name'].upper()
            if item_club == club:
                #json_data['items'][0]['nation']['name']
                list_players={'name':items['commonName'],'position':items['position'],'nation':items['nation']['name']}
                players.append(list_players)
                data_respuesta={'page': json_data['page'],
                        'totalpages':json_data['totalPages'],
                        'items':len(players),
                        'totalItems':len(json_data['items']),
                        'Players':players
                        
                        }

        return Response(data_respuesta)
    


class PlayersRequestViewSet(viewsets.ModelViewSet):
    
    serializer_class = PlayersRequestSerializers
    queryset = PlayersRequest.objects.all()
    
    def create(self,request,*args, **kwargs):
        datos = request.data
        #datos['page']
        #json_data['items'][0]['club']['name']
        url = requests.get('https://www.easports.com/fifa/ultimate-team/api/fut/item?page={}&name={}'.format(datos['page'],datos['name']))
        json_data=url.json()
        #club = datos['name'].upper()
        players = []
        data_respuesta={}
        for items in json_data['items']: 
                #json_data['items'][0]['nation']['name']
            list_players={'name':items['commonName'],'position':items['position'],'nation':items['nation']['name']}
            players.append(list_players)
            data_respuesta={'page': json_data['page'],
                    'totalpages':json_data['totalPages'],
                    'items':len(players),
                    'totalItems':len(json_data['items']),
                    'Players':players
                    }
        
        return Response(data_respuesta)