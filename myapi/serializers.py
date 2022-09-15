from rest_framework import serializers
from .models import File

#inherit it from serializer.ModelSerializer (not from serializer.Serializer) because it is directly attached to a model object
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
        #The fields can either be a list of attributes on the model or a string with the value __all__. 
