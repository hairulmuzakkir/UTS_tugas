from imsyakApp.models import jadwalModels
from rest_framework import serializers

class jadwalSerializer(serializers.ModelSerializer):
    class Meta:
        model =  jadwalModels
        fields = ['id','Tanggal','Imsyak','Subuh','Terbit','Duha','Zuhur', 'Asar','Magrib','Isya']