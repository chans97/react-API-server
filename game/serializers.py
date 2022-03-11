from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinValueValidator)
from rest_framework import serializers
from .models import GameUser,Repl


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(validators=[MaxLengthValidator(20)])

    class Meta:
        model = GameUser
        fields = ['id', 'title']




class PostDetailSerializer(serializers.ModelSerializer):

    title = serializers.CharField(validators=[MaxLengthValidator(20)])
    contents = serializers.CharField(validators=[MaxLengthValidator(1000)])
    repls = serializers.StringRelatedField(many=True)
    class Meta:
        model = GameUser
        fields = ('id','title', 'contents', 'repls')
        # fields = ('title', 'contents')

class ReplSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repl
        fields = ('id','contents', 'post')