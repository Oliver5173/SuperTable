using Requests
using JSON
include("timeInfo.jl")
import Requests:get,json

courseAPI = "http://www.sfu.ca/bin/wcm/course-outlines?"


function get_API(inputLink,key)
  if key == ""
    link = inputLink
  elseif inputLink == "http://www.sfu.ca/bin/wcm/course-outlines?"
    link = string(inputLink,key)
  else
    link = string(inputLink,"/",key)
  end
  info = getCourseInfo(link)
  if info != -1
    println(info)
  end
  res = get(link)
  jsonFile = JSON.parse(IOBuffer(res.data))
  for ele in jsonFile
    try haskey(ele,"value")
      get_API(link,ele["value"])
    catch
      return ele
    end
  end
end
