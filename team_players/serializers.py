from rest_framework import serializers
from .models import PlayersRequest,TeamsRequest

# class TeamsRequestSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = TeamsRequest
#         fields= '__all__'

class TeamRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamsRequest
        fields= ('team','page')
        
class PlayersRequestSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlayersRequest
        fields= ('name','page')