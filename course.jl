function get_API(inputLink,key,db)
  if key == ""
    link = inputLink
  elseif inputLink == "http://www.sfu.ca/bin/wcm/course-outlines"
    #info = getCourseInfo("http://www.sfu.ca/bin/wcm/course-outlines?2017/summer/cmpt/300/d100")
    link = string(inputLink,key)
  else
    link = string(inputLink,"/",key)
  end
  println(link)
  info = getCourseInfo(link)
  if info != -1
    println(length(info.class))
    print_with_color(:red,string(link,"\n"))
    courseInfo = split(info.courseName," ")
    tableName = string(lowercase(courseInfo[1]),"x")
    examDate = split(info.exam.startDate," ")
    examstartTime = length(examDate) == 1 ? "NULL": info.exam.startTime
    examEndTime = length(examDate) == 1 ? "NULL": info.exam.endTime
    examDate = length(examDate) == 1 ? "NULL": string(examDate[1]," ",examDate[2]," ",examDate[3]," "examDate[6])
    #=
    SQLite.query(db,"create table $(dep)(course TEXT,section TEXT,
                                         campus TEXT,sectionCode TEXT,
                                         startTime1 TIME,endTime1 TIME,days1 TEXT,
                                         startTime2 TIME,endTime2 TIME,days2 TEXT,
                                         startTime3 TIME,endTime3 TIME,days3 TEXT,
                                         examstartTime TIME,examEndTime TIME,examDate TEXT)")
    =#
    if length(info.class) == 1
      SQLite.query(db,"insert into $tableName values('$(courseInfo[2])','$(courseInfo[3])',
                                                     '$(info.campus)','$(info.class[1].sectionCode)',
                                                     '$(info.class[1].startTime)','$(info.class[1].endTime)','$(info.class[1].days)',
                                                      NULL,NULL,NULL,
                                                      NULL,NULL,NULL,
                                                     '$(examstartTime)','$(examEndTime)','$(examDate)')")
    elseif length(info.class) == 2
      SQLite.query(db,"insert into $tableName values('$(courseInfo[2])','$(courseInfo[3])',
                                                     '$(info.campus)','$(info.class[1].sectionCode)',
                                                     '$(info.class[1].startTime)','$(info.class[1].endTime)','$(info.class[1].days)',
                                                     '$(info.class[2].startTime)','$(info.class[2].endTime)','$(info.class[2].days)',
                                                      NULL,NULL,NULL,
                                                      '$(info.exam.startTime)','$(info.exam.endTime)','$(examDate)')")
    elseif length(info.class) == 3
      SQLite.query(db,"insert into $tableName values('$(courseInfo[2])','$(courseInfo[3])',
                                                     '$(info.campus)','$(info.class[1].sectionCode)',
                                                     '$(info.class[1].startTime)','$(info.class[1].endTime)','$(info.class[1].days)',
                                                     '$(info.class[2].startTime)','$(info.class[2].endTime)','$(info.class[2].days)',
                                                     '$(info.class[3].startTime)','$(info.class[3].endTime)','$(info.class[3].days)',
                                                     '$(info.exam.startTime)','$(info.exam.endTime)','$(examDate)')")
    end
    println(info)
  end
  res = get(link)
  jsonFile = JSON.parse(IOBuffer(res.data))
  for ele in jsonFile
    try haskey(ele,"value")
      get_API(link,ele["value"],db)
    catch
      return ele
    end
  end
end


type courseSchedule
  startTime :: String
  endTime :: String
  days :: String
  sectionCode :: String
end

type examSchedule
  startTime :: String
  endTime :: String
  startDate ::String
end

type course
  courseName :: String
  campus :: String
  class :: Array{courseSchedule}
  exam :: examSchedule
end

function getCourseInfo(url)
  try
#=   json_info = json(get(string(base_url
                                , year ,"/"
                                , term , "/"
                                , department , "/"
                                , courseNumber , "/"
                                , courseSection)))
=#
    json_info = json(get(url))
    class = Array{courseSchedule}(length(json_info["courseSchedule"]))
    for i in 1 : length(json_info["courseSchedule"])
      class[i] = courseSchedule(json_info["courseSchedule"][i]["startTime"],
                              json_info["courseSchedule"][i]["endTime"],
                              json_info["courseSchedule"][i]["days"],
                              json_info["courseSchedule"][i]["sectionCode"])
    end
    try
      exam = examSchedule(json_info["examSchedule"][1]["startTime"],
                          json_info["examSchedule"][1]["endTime"],
                          json_info["examSchedule"][1]["startDate"])
      return course(json_info["info"]["name"],json_info["courseSchedule"][1]["campus"],class,exam)
    end
    return course(json_info["info"]["name"],json_info["courseSchedule"][1]["campus"],class,examSchedule("","",""))
  catch
    return -1
  end
end

function getDepartment(year,term)
  department_info = json(get(string(base_url,year,"/",term)))
  department_arr = Array{String}(0)
  #add "x" to avoid SQL keywords
  for i in department_info
    push!(department_arr,string(i["value"],"x"))
  end
  return department_arr
end
