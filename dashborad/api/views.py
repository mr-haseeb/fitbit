from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from dashborad.models import Health
from dashborad.api.serializer import HealthSerializer


@api_view(['GET'])
def api_detail_health_view(request,slug):
    try:
        health=Health.objects.get(slug=slug)
    
    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer=HealthSerializer(health)
        return Response(serializer.data)


@api_view(['PUT'])
def api_update_health_view(request,slug):

    try:
        health =Health.objects.get(slug=slug)
    
    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="PUT":
        serializer=HealthSerializer(health,data=request.data)
        data={}

        if serializer.is_valid():
            serializer.save()
            data["success"]="update sucessful"
            return Response(data=data)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def api_delete_health_view(request,slug):

    try:
        health =Health.objects.get(slug=slug)
    
    except Health.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="DELETE":
        operation=health.delete()
        data={}

        if operation:
            data['successs']="delete successful"
        
        else:
            data["failure"]="delete failed "

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def api_post_health_view(request):

    health=Health.objects.get(pk=1)

    if request.method=='POST':
        serializer=HealthSerializer(health,data=request.data)
        data={}

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        



