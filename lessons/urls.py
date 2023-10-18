from django.urls import path
from .views import LessonsList, LessonDetail, InstructorDetail,InstructorsList, SeriesList, StylesList, LessonsBySerie, SerieDetail

urlpatterns = [
    path('lessons/', LessonsList.as_view()),
    path('lessons/<int:pk>/', LessonDetail.as_view()),
    path('instructors/', InstructorsList.as_view()),
    path('<int:pk>/instructor/', InstructorDetail.as_view()),
    path('series/', SeriesList.as_view()),
    path('series/<int:pk>/', SerieDetail.as_view()),
    path('series/<int:pk>/lessons/', LessonsBySerie.as_view()),
    path('styles/', StylesList.as_view()),
    
]