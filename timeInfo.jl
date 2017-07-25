using Requests
import Requests: get,json

type courseSchedule
  startTime :: String
  endTime :: String
  roomNumber :: String
  days :: String
  sectionCode :: String
end

type examSchedule
  startTime :: String
  endTime :: String
  startDate ::String
end

type course
  class :: Array{courseSchedule}
  exam :: examSchedule
end


const base_url = "http://www.sfu.ca/bin/wcm/course-outlines?"
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
                              json_info["courseSchedule"][i]["roomNumber"],
                              json_info["courseSchedule"][i]["days"],
                              json_info["courseSchedule"][i]["sectionCode"])
    end
    try
      exam = examSchedule(json_info["examSchedule"][1]["startTime"],
                          json_info["examSchedule"][1]["endTime"],
                          json_info["examSchedule"][1]["startDate"])
      return course(class,exam)
    end
    return course(class,examSchedule("","",""))
  catch
    return -1
  end
end
