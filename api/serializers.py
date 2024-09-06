# serves to serializes data befere being rendered
# creates serializer for Item model and convert instances of the object model 
# to data type that Responce object can understand

from rest_framework import serializers
from base.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'



