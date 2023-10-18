from django.contrib import admin
from lessons.models import Lesson, Instructor, Skill, Discipline, Serie, Style

# Register your models here.
# class LessonAdmin(admin.ModelAdmin):
#     pass
# class InstructorAdmin(admin.ModelAdmin):
#     pass
# class SkillAdmin(admin.ModelAdmin):
#     pass
# class DisciplineAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Skill)
admin.site.register(Discipline)
admin.site.register(Serie)
admin.site.register(Style)