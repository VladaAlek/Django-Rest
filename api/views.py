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


#view to add data to DB
# uses serializer to pass all data from the Item model

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)