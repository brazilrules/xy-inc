from rest_framework import serializers
from rest_api.models import POI

class POISerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=50)
    coord_x = serializers.IntegerField()
    coord_y = serializers.IntegerField()
    
    def create(self, validated_data):
        return POI.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.coord_x = validated_data.get('coord_x', instance.coord_x)
        instance.coord_y = validated_data.get('coord_y', instance.coord_y)
        instance.save()
        return instance