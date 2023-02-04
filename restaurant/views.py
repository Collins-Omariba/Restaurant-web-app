from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .forms import BookingForm
from .models import BookingTemplate, MenuTemplate, Booking, Menu
from  .serializers import BookingSerializer, MenuSerializer

# template views
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)



def menu(request):
    menu_data = MenuTemplate.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = MenuTemplate.objects.get(pk=pk)
    else:
        menu_item = ''

    menu = {'menu_item': menu_item}
    return render(request, 'menu_item.html', menu)

    

#drf api endpoints class base views

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

class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated]