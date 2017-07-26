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
    SQLite.query(db,"create table $(dep)(course TEXT,
                                         section TEXT,
                                         campus TEXT,
                                         sectionCode TEXT,
                                         startTime1 TEXT,endTime1 TEXT,days1 TEXT,
                                         startTime2 TEXT,endTime2 TEXT,days2 TEXT,
                                         startTime3 TEXT,endTime3 TEXT,days3 TEXT,
                                         examStartTime TEXT,examEndTime TEXT,
                                         examStartDate TEXT)")
  end
  get_API(string(base_url,year,"/",term),"")
end
