from rest_framework.response import Response
# Response class will take python data and render it in JSON format
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer


@api_view(['GET'])
def getData(request):
    items =Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)
