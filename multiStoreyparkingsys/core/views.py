from heapq import heappush, heappop, heapify
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CarSerializer
from .models import Car, SlotsAvailable

heap_slots = []
heapify(heap_slots)
for i in range(1, 100):
    heappush(heap_slots, i)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def CarEnter(request):
    if request.method == 'POST':
        cs = heappop(heap_slots)
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(slot=cs)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def CarLeaves(request, pk):
    if request.method == 'DELETE':
        CarObject = get_object_or_404(Car, pk=pk)
        heappush(heap_slots, CarObject.slot)
        CarObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
