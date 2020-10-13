from rest_framework.serializers import ModelSerializer


from .models import Contact, AboutUs

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AboutSerializer(ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'