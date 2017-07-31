from django.db import models
from collections import OrderedDict
import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Create your models here.
class SearchRequest(models.Model):
    year = models.TextField()
    semester = models.TextField()
    preference = models.TextField()
    department = models.TextField()
    courseNum = models.TextField()

    def __str__(self):
        return self.department+str(self.courseNum) 

    def __init__(self, year, semester, preference, department, courseNum):
        self.year = year
        self.semester = semester
        self.preference = preference
        self.department = department
        self.courseNum = courseNum
        
        self.cursor = None
        self.rtnDict = OrderedDict()

    def searchFromDB(self):
        dbName = str(self.year) + self.semester.lower() + ".db"
        connectDB = sqlite3.connect(dbName)
        connectDB.row_factory = dict_factory
        query = "SELECT * FROM " + (self.department+"x") + " WHERE course=" + str(self.courseNum) + " AND sectionCode=" + "LEC"
        self.cursor = connectDB.execute(query)

    def filterPrefer(self):
        courseOrder = 0
        if self.preference == "All":
            for row in self.cursor:
                self.rtnDict[courseOrder] = row
                courseOrder += 1
        elif self.preference == "Morning":
            for row in self.cursor:
                if int(row["endTime1"].split(":")[0]) <= 14:
                    self.rtnDict[courseOrder] = row 
                    courseOrder += 1
        elif self.preference == "Afternoon":
            for row in self.cursor:
                if int(row["startTime1"].split(":")[0]) >= 14:
                    self.rtnDict[courseOrder] = row 
                    courseOrder += 1            

    def get_rtnVal(self):
        self.searchFromDB()
        self.filterPrefer()
        return self.rtnDict    

        

class SearchResult(models.Model): 
    department = models.TextField()
    courseNum = models.TextField()
    courseCampus = models.TextField()
    courseRoom = models.TextField()
    courseStarTime = models.TimeField()
    courseEndTime = models.TimeField()
    courseDays = models.TextField()
    courseExamTime = models.TimeField()
    courseExamDate = models.DateField()

    def __str__(self):
        return self.department+str(self.courseNum) 