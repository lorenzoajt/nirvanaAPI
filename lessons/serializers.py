from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Lesson, Instructor, Serie

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class LessonSerializer(serializers.ModelSerializer):
    discipline = serializers.StringRelatedField(many=True)
    skill = serializers.StringRelatedField(many=True)
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonOverviewSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Lesson
        fields = ['id', 'title', 'instructor', 'image_link']

class InstructorSerializer(serializers.ModelSerializer):
    discipline = serializers.StringRelatedField(many=True)
    class Meta:
        model = Instructor
        fields = ['id', 'name', 'picture', 'discipline', 'bio']

class SerieSerializer(serializers.ModelSerializer):
    instructor = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Serie
        fields = '__all__'