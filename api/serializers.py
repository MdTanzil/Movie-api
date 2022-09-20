from rest_framework import serializers
from . models import Movie
class MovieSerializer(serializers.ModelSerializer):

    genre= serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

