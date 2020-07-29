from rest_framework import serializers
from .models import Todo, Just, UpStat


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'



class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model=Just
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpStat
        fields =['stat']