import requests
import json

SFU_API = "http://www.sfu.ca/bin/wcm/academic-calendar?{year}/{term}/courses/{paramemters}"
YEAR = input("YEAR: ?")
TERM = input("TERM: ?")
PARAMEMTERS = input("COURSE#: ?").lower()

NEW_QUERY = SFU_API.format(year=YEAR, term=TERM, paramemters=PARAMEMTERS)
print(NEW_QUERY)
RES = requests.get(NEW_QUERY)
print(RES.json())

