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
    examstartTime = length(examDate) == 1 ? NULL: info.exam.startTime
    examEndTime = length(examDate) == 1 ? NULL: info.exam.endTime
    examDate = length(examDate) == 1 ? NULL: string(examDate[1]," ",examDate[2]," ",examDate[3]," ",examDate[6])
    startDate = split(info.startDate," ")
    startDate = length(startDate) == 1 ? NULL: string(startDate[1]," ",startDate[2]," ",startDate[3]," ",startDate[6])
    endDate = split(info.endDate," ")
    endDate = length(endDate) == 1 ? NULL: string(endDate[1]," ",endDate[2]," ",endDate[3]," ",endDate[6])
    #=
    SQLite.query(db,"create table $(dep)(course TEXT,section TEXT,
                                         campus TEXT,sectionCode TEXT,
                                         startTime1 TIME,endTime1 TIME,days1 TEXT,
                                         startTime2 TIME,endTime2 TIME,days2 TEXT,
                                         startTime3 TIME,endTime3 TIME,days3 TEXT,
                                         examstartTime TIME,examEndTime TIME,examDate TEXT,
                                         startDate TEXT,endDate TEXT)")
    =#
    if length(info.class) == 1
      SQLite.query(db,"insert into $tableName values('$(courseInfo[2])','$(courseInfo[3])',
                                                     '$(info.campus)','$(info.class[1].sectionCode)',
                                                     '$(info.class[1].startTime)','$(info.class[1].endTime)','$(info.class[1].days)',
                                                      NULL,NULL,NULL,
                                                      NULL,NULL,NULL,
                                                     '$(examstartTime)','$(examEndTime)','$(examDate)',
                                                     '$(startDate)','$(endDate)')")
    elseif length(info.class) == 2
      SQLite.query(db,"insert into $tableName values('$(courseInfo[2])','$(courseInfo[3])',
                                                     '$(info.campus)','$(info.class[1].sectionCode)',
                                                     '$(info.class[1].startTime)','$(info.class[1].endTime)','$(info.class[1].days)',
                                                     '$(info.class[2].startTime)','$(info.class[2].endTime)','$(info.class[2].days)',
                                                      NULL,NULL,NULL,
                                                      '$(info.exam.startTime)','$(info.exam.endTime)','$(examDate)',
                                                      '$(startDate)','$(endDate)')")
    elseif length(info.class) == 3
      SQLite.query(db,"insert into $tableName values('$(courseInfo[2])','$(courseInfo[3])',
                                                     '$(info.campus)','$(info.class[1].sectionCode)',
                                                     '$(info.class[1].startTime)','$(info.class[1].endTime)','$(info.class[1].days)',
                                                     '$(info.class[2].startTime)','$(info.class[2].endTime)','$(info.class[2].days)',
                                                     '$(info.class[3].startTime)','$(info.class[3].endTime)','$(info.class[3].days)',
                                                     '$(info.exam.startTime)','$(info.exam.endTime)','$(examDate)',
                                                     '$(startDate)','$(endDate)')")
    end
    println(info)
  end
  res = get(link)
  jsonFile = JSON.parse(IOBuffer(res.data))
  @parallel for ele in jsonFile
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
  startDate :: String
  endDate :: String
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
      exam = examSchedule(json_info["examSchedule"][end]["startTime"],
                          json_info["examSchedule"][end]["endTime"],
                          json_info["examSchedule"][end]["startDate"])
      return course(json_info["info"]["name"],json_info["courseSchedule"][1]["campus"],class,exam,
                    json_info["courseSchedule"][1]["startDate"],json_info["courseSchedule"][1]["endDate"])
    end
    return course(json_info["info"]["name"],json_info["courseSchedule"][1]["campus"],class,examSchedule("","",""),
                  json_info["courseSchedule"][1]["startDate"],json_info["courseSchedule"][1]["endDate"])
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
