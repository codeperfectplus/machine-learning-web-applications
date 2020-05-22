from rest_framework import serializers
from .models import IrisModel

class IrisModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IrisModel
        fields = ('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
