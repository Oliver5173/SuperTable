using SQLite
using Requests
using JSON
include("course.jl")
import Requests:get,json

const base_url = "http://www.sfu.ca/bin/wcm/course-outlines?"

function update_db(year,term)
  department_arr = getDepartment(year,term)
  db = SQLite.DB(string(year,term,".db"))
  for dep in department_arr
    SQLite.query(db,"create table $(dep)(course TEXT,section TEXT,
                                         campus TEXT,sectionCode TEXT,
                                         startTime1 TIME,endTime1 TIME,days1 TEXT,
                                         startTime2 TIME,endTime2 TIME,days2 TEXT,
                                         startTime3 TIME,endTime3 TIME,days3 TEXT,
                                         examstartTime TIME,examEndTime TIME,examDate TEXT)")
  end
  get_API(string(base_url,year,"/",term),"",db)
end
