from django.db import models

# Create your models here.
class SearchRequest(models.Model):
    year = models.IntegerField()
    semester = models.TextField()
    courseInfo = models.TextField()

    def __str__(self):
        return self.courseInfo

class SearchRequestModify(models.Model):
    year = models.IntegerField()
    semester = models.TextField()
    department = models.TextField()
    courseNum = models.IntegerField()

    def __str__(self):
        return self.department+str(self.courseNum) 

class SearchResult(models.Model): 
    department = models.TextField()
    courseNum = models.IntegerField()
    courseCampus = models.TextField()
    courseRoom = models.TextField()
    courseStarTime = models.TimeField()
    courseEndTime = models.TimeField()
    courseDays = models.TextField()
    courseExamTime = models.TimeField()
    courseExamDate = models.DateField()

    def __str__(self):
        return self.department+str(self.courseNum) 