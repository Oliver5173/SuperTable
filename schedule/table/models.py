import time,re
from django.db import models

# Create your models here.
class Course(models.Model):
    year = models.TextField()
    semester = models.TextField()
    searchContent = models.TextField()
    currentTime = None

    def __init__(self,year,semester,content):
         self.year = year
         self.semester = semester
         self.searchContent =  content
         self.currentTime = time.localtime()
         self.currentTime = (str(self.currentTime[0]) + "." +str(self.currentTime[1]) + "." +str(self.currentTime[2]) + " " +
                                         str(self.currentTime[3]) + ":" + str(self.currentTime[4])) #year.mo.day ho:min

    def __str__(self):
          return self.currentTime + "=" + str(self.searchContent)
    
    def splitter(content):
        courseList = []
        course_split = content.split(';')
        for course in course_split:
            index_firstDigit = re.search("\d",course) #return <match>
            if index_firstDigit is not None:
                courseList.append((course[:index_firstDigit.start()],course[index_firstDigit.start():]))
        return courseList # Array<tuple> [(department,#)]

     
        
