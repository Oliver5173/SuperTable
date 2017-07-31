$(document).ready(function() {
    var rtnDict = "{{ rtnDict}}";
    $('#calendar').fullCalendar({
        schedulerLicenseKey: 'CC-Attribution-NonCommercial-NoDerivatives',
        defaultView: 'agendaWeek',
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay,listWeek'
        },
        minTime: '08:00:00',
        maxTime: '22:00:00',
        slotDuration: '00:30:00',
        navLinks: true, // can click day/week names to navigate views
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        rtnDict
    });

});

