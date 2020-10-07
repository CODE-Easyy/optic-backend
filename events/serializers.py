from rest_framework import serializers

from .models import Event

class SlideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id',
                  'img_slide',
                  'is_active',)

class DetailEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id',
                  'img',
                  'title',
                  'description',
                  'is_active',
                  'from_date',
                  'to_date',
                  'products')