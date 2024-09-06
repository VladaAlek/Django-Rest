from rest_framework.response import Response
# Response class will take python data and render it in JSON format
from rest_framework.decorators import api_view

@api_view
def getData(request):
    person = {'name':'Denis', 'age': 28}
    return Response(person)
