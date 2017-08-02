$(document).ready(function(){
    var date = new Date();
    var month = date.getMonth();
    var year = date.getFullYear();
    var semester = "Fall";
    if (month > 9){
        semester = "Spring";
    }
    else if (month > 4){
        semester = "Fall";
    }
    else{
        semester = "Summer";
    }
    $("#year").val(year.toString());
    $("#semester").val(semester);
    $("#preference").val("All");
});