from django.urls import path
from .views import LessonsList, LessonDetail, InstructorDetail,InstructorsList, SeriesList

urlpatterns = [
    path('lessons/', LessonsList.as_view()),
    path('lessons/<int:pk>/', LessonDetail.as_view()),
    path('instructors/', InstructorsList.as_view()),
    path('<int:pk>/instructor/', InstructorDetail.as_view()),
    path('series/', SeriesList.as_view()),
]