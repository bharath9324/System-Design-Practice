from rest_framework import viewsets
from django.http import HttpResponse

from backend.serializers import VisitorSerializer
from backend.models import Visitor
from backend.serializers import HotelSerializer
from backend.models import Hotel




class VisitorViewSet(viewsets.ModelViewSet):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


def abc(request):
	return HttpResponse("<h1>HELLO<h1>")