from django.db import models
from collections import OrderedDict
import sqlite3
import json

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

    def __init__(self, year, semester, preference, department, courseNum,courseTimes):
        self.year = year
        self.semester = semester
        self.preference = preference
        self.department = department
        self.courseNum = courseNum
        
        self.connectDB = None
        self.cursor = None
        # self.rtnDict = OrderedDict()
        self.rtnDict = OrderedDict()
        self.courseTimes = courseTimes

    def searchFromDB(self):
        dbName = str(self.year) + self.semester.lower() + ".db"
        self.connectDB = sqlite3.connect(dbName)
        self.connectDB.row_factory = dict_factory
        query = "SELECT * FROM " + (self.department+ "x") + " WHERE course=" + str(self.courseNum) + " AND sectionCode='LEC'"
        self.cursor = self.connectDB.execute(query)
    
    def parseMonth(self,abbr):
        monthDict = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04",
                    "May":"05", "June":"06", "July":"07", "Aug":"08",
                    "Sept":"09", "Oct":"10", "Nov":"11", "Dec":"12",}
        return monthDict[abbr]

    def parseWeekday(self, abbr):
        weekdayDict = {"Mo":1, "Tu":2,
                        "We":3, "Th":4,
                        "Fr":5,}
        return weekdayDict[abbr]

    def parseDictRow(self,row):
        classRow = {}
        # row for final exam
        finalRow = {}
        if row["startTime1"]:
            classRow["title"] = self.department + self.courseNum
            classRow["start"] = row["startTime1"]
            classRow["end"] = row["endTime1"]
            classRow["dow"] = [self.parseWeekday(day.strip()) for day in row["days1"].split(",")]
            self.rtnDict[self.courseTimes] = classRow
            self.courseTimes += 1
        if row["examDate"]:
            dateFormList =[part.strip() for part in row["examDate"].split(" ")]
            dateForm = dateFormList[3] + "-" + self.parseMonth(dateFormList[1]) +"-" + dateFormList[2] + "T"
            finalRow["titile"] = self.department + self.courseNum + " Final"
            finalRow["start"] = dateForm + row["examstartTime"] + ":00"
            finalRow["end"] = dateForm + row["examEndTime"] + ":00"
            self.rtnDict[self.courseTimes] = finalRow
            self.courseTimes += 1


    def filterPrefer(self):
        if self.preference == "All":
            for row in self.cursor:
                self.parseDictRow(row)
        elif self.preference == "Morning":
            for row in self.cursor:
                if int(row["endTime1"].split(":")[0]) <= 14:
                    self.parseDictRow(row)
        elif self.preference == "Afternoon":
            for row in self.cursor:
                if int(row["startTime1"].split(":")[0]) >= 14:
                    self.parseDictRow(row) 

    def get_rtnVal(self):
        self.searchFromDB()
        self.filterPrefer()
        self.connectDB.rollback()
        self.connectDB.close()
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