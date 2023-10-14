from django.db import models


class Lesson(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    summary = models.TextField(max_length=1000)
    serie = models.ForeignKey('Serie', null=True, blank=True, on_delete=models.CASCADE)
    instructor = models.ManyToManyField('Instructor')
    discipline = models.ManyToManyField('Discipline')
    skill = models.ManyToManyField('Skill')
    duration = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    image_link = models.CharField(max_length=100)
    video_link = models.CharField(max_length=100)
    intensity = models.IntegerField()
    difficulty = models.IntegerField()

    def __str__(self):        
        return self.title
    
class Serie(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)    
    instructor = models.ManyToManyField('Instructor')
    discipline = models.ManyToManyField('Discipline')
    skill = models.ManyToManyField('Skill')
    image_link = models.CharField(max_length=100)
    video_link = models.CharField(max_length=100)
    intensity = models.IntegerField()
    difficulty = models.IntegerField()

    def __str__(self):        
        return self.name


class Instructor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    bio = models.TextField(max_length=1000)
    discipline = models.ManyToManyField('Discipline')
    facebook = models.CharField(max_length=100, null=True, blank=True, default='')
    instagram = models.CharField(max_length=100, null=True, blank=True, default='')
    website = models.CharField(max_length=100, null=True, blank=True, default='')
    picture = models.CharField(max_length=100, default='')

    def __str__(self):        
        return self.name


class Discipline(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    
    def __str__(self):        
        return self.name

class Skill(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    
    def __str__(self):        
        return self.name