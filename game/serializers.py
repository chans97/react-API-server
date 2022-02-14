from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinValueValidator)
from rest_framework import serializers
from .models import GameUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(validators=[MaxLengthValidator(6)])
    level = serializers.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        model = GameUser
        fields = ['url', 'id', 'name', 'level']