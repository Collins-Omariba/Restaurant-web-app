from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Booking, Menu
from  .serializers import BookingSerializer, MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})



class BookingView(APIView):

    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookingSerializer

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})


class MenuItemView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

	def get_permissions(self):
		permission_classes = []
		if self.request.method != 'GET':
			permission_classes = [IsAuthenticated]
		return [permission() for permission in permission_classes]




class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuSerializer

	def get_permissions(self):
		permission_classes = []
		if self.request.method != 'GET':
			permission_classes = [IsAuthenticated]
		return [permission() for permission in permission_classes]
