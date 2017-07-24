import requests
import json

SFU_API = "http://www.sfu.ca/bin/wcm/academic-calendar?{year}/{term}/courses/{paramemters}"
YEAR = input("YEAR: ?")
TERM = input("TERM: ?")
PARAMEMTERS = input("COURSE#: ?").lower().split(" ")
for PARAMEMTER in PARAMEMTERS:
    print(PARAMEMTER)
    NEW_QUERY = SFU_API.format(year=YEAR, term=TERM, paramemters=PARAMEMTER)
    RES = requests.get(NEW_QUERY)
    print(RES.json())
print(NEW_QUERY)
RES = requests.get(NEW_QUERY)
print(RES.json())

