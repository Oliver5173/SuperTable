using Requests
using JSON

courseAPI = "http://www.sfu.ca/bin/wcm/course-outlines?"


function get_API(inputLink,key)
  if key == ""
    link = inputLink
  elseif inputLink == "http://www.sfu.ca/bin/wcm/course-outlines?"
    println(1)
    link = string(inputLink,key)
  else
    link = string(inputLink,"/",key)
  end
  println(link)
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

get_API(courseAPI,"")
