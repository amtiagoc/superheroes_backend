
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Superheroe
from .serializers import SuperheroeSerializer
from rest_framework import serializers
from rest_framework import status


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Listar': '/listar/',
        'Crear': '/crear/',
        'Actualizar': '/actualizar/<str:pk>/',
        'Eliminar': '/eliminar/<str:pk>/',
        }
    return Response(api_urls)


@api_view(['POST'])
def add_superheroe(request):
    superheroe = SuperheroeSerializer(data=request.data)
  
    # validating for already existing data
    if Superheroe.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if superheroe.is_valid():
        superheroe.save()
        return Response(superheroe.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_superheroe(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        superheroes = Superheroe.objects.filter(**request.query_param.dict())
    else:
        superheroes = Superheroe.objects.all()
  
    # if there is something in items else raise error
    if superheroes:
        serializer = SuperheroeSerializer(superheroes, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# Hacer update de un superheroe
@api_view(['PUT'])
def update_superheroe(request, pk):
    superheroe = Superheroe.objects.get(id=pk)
    serializer = SuperheroeSerializer(instance=superheroe, data=request.data)
    print(request.data)
    # validating for already existing data
    if Superheroe.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This superheroe already exists')
  
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_superheroe(request, pk):
    superheroe = Superheroe.objects.get(pk=pk)
    if superheroe:
        superheroe.delete()
        return Response(f'{superheroe.nombre} successfully deleted!')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    