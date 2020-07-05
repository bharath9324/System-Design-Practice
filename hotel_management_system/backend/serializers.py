from rest_framework import serializers

from backend.models import Visitor
from backend.models import Hotel


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'

    def validate(self, data):
    	import pdb; pdb.set_trace()
    	return data


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

