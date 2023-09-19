from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from .serializers import UserSerializer, GroupSerializer, LessonSerializer, LessonOverviewSerializer, InstructorSerializer
from .models import Lesson, Discipline, Instructor, Skill
from rest_framework.views import APIView
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class LessonsList(generics.GenericAPIView):    
    queryset = Lesson.objects.all()
    def get(self, request):
        try:
            lessons = Lesson.objects.all()
            serializer = LessonOverviewSerializer(lessons, many=True)
            return Response(serializer.data)            
        except Exception as E:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LessonDetail(generics.RetrieveAPIView):    
    queryset = Lesson.objects.all()

    def get(self, request, pk):
        try:        
            lesson = Lesson.objects.get(pk=pk)
            serializer = LessonSerializer(lesson)
            return Response(serializer.data)   
        except Exception as E:
            return Response(data={E.args[0]}, status=status.HTTP_404_NOT_FOUND)

class InstructorsList(generics.GenericAPIView):    
    queryset = Instructor.objects.all()
    def get(self, request):
        try:
            instructors = Instructor.objects.all()
            serializer = InstructorSerializer(instructors, many=True)
            return Response(serializer.data)            
        except Exception as E:
            return Response(status=status.HTTP_404_NOT_FOUND)


class InstructorDetail(generics.RetrieveAPIView):  
    queryset = Instructor.objects.all()  
    def get(self, request, pk):
        try:                    
            instructor = Instructor.objects.filter(lesson__id= pk)
            serializer = InstructorSerializer(instructor, many=True)
            return Response(serializer.data)   
        except Exception as E:
            return Response(data={E.args[0]}, status=status.HTTP_404_NOT_FOUND)