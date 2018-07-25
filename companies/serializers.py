from rest_framework import serializers
from . models import LoginDB


class LoginDBserializer(serializers.ModelSerializer):
    class Meta:
        model = LoginDB
        fields = ('Manual_id','Full_name')

        #fields =  '__all__'