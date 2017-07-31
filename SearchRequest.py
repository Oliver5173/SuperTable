import sqlite3
import re

class SearchRequest():
    def __init__(self,infoDict):
        self.infoDict = infoDict
        self.year = infoDict['year']
        self.semester = infoDict['semester']
        self.courseList = infoDict['courseList']
        self.courseDict = {}

        match = re.match(r"([a-z]+)([0-9]+)",str, re.I)

    def seperateDepartment(self):

            pass
