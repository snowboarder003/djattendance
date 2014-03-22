/**
* Sets up the weekly schedule (Monday - Lord's day) and loads and displays the events, if any.
*
*/
jQuery(document).ready(function($) {

   var $calendar = $('#calendar');
   var id = 10;

   $calendar.weekCalendar({
      // unchanging display settings
      timeslotsPerHour : 4,
      allowCalEventOverlap : false,
      overlapEventsSeparate: true,
      firstDayOfWeek : 1,
      longDays : ["Lord's day", 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
      businessHours :{start: 6, end: 24, limitDisplay: true },
      daysToShow : 7,

      // calculated display settings
      height : function($calendar) {
         return $(window).height();
      },
      eventRender : function(calEvent, $event) {
         if (calEvent.end.getTime() < new Date().getTime()) {
            $event.css("backgroundColor", "#aaa");
            $event.find(".wc-time").css({
               "backgroundColor" : "#999",
               "border" : "1px solid #888"
            });
         }
      },
      draggable : function(calEvent, $event) {
         return calEvent.readOnly != true;
      },
      resizable : function(calEvent, $event) {
         return calEvent.readOnly != true;
      },
      eventNew : function(calEvent, $event) {
         var $dialogContent = $("#event_edit_container");
         resetForm($dialogContent);
         var startField = $dialogContent.find("select[name='start']").val(calEvent.start);
         var endField = $dialogContent.find("select[name='end']").val(calEvent.end);
         var titleField = $dialogContent.find("input[name='title']");
         var typeField = $dialogContent.find("input[name='eventType']");
         var bodyField = $dialogContent.find("textarea[name='body']");

         $dialogContent.dialog({
            modal: true,
            title: "New Scheduled Event",
            close: function() {
               $dialogContent.dialog("destroy");
               $dialogContent.hide();
               $('#calendar').weekCalendar("removeUnsavedEvents");
            },
            buttons: {
               save : function() {
                  calEvent.id = id;
                  id++;
                  calEvent.start = new Date(startField.val());
                  calEvent.end = new Date(endField.val());
                  calEvent.title = titleField.val();
                  calEvent.body = bodyField.val();
                  calEvent.eventType = typeField.val();

                  $calendar.weekCalendar("removeUnsavedEvents");
                  $calendar.weekCalendar("updateEvent", calEvent);
                  $dialogContent.dialog("close");
               },
               cancel : function() {
                  $dialogContent.dialog("close");
               }
            }
         }).show();

         $dialogContent.find(".date_holder").text($calendar.weekCalendar("formatDate", calEvent.start));
         setupStartAndEndTimeFields(startField, endField, calEvent, $calendar.weekCalendar("getTimeslotTimes", calEvent.start));

      },
      eventDrop : function(calEvent, $event) {
      },
      eventResize : function(calEvent, $event) {
      },
      eventClick : function(calEvent, $event) {

         // shade darker to select for attendance - example
         if (calEvent.readOnly) {
            // TODO: toggle colour
            $event.css("backgroundColor", "rgb(77, 72, 72)");
            return;
         }

         var $dialogContent = $("#event_edit_container");
         resetForm($dialogContent);
         var startField = $dialogContent.find("select[name='start']").val(calEvent.start);
         var endField = $dialogContent.find("select[name='end']").val(calEvent.end);
         var titleField = $dialogContent.find("input[name='title']").val(calEvent.title);
         var bodyField = $dialogContent.find("textarea[name='body']");
         var typeField = $dialogContent.find("input[name='eventType']");

         bodyField.val(calEvent.body);

         $dialogContent.dialog({
            modal: true,
            title: "Edit - " + calEvent.title,
            close: function() {
               $dialogContent.dialog("destroy");
               $dialogContent.hide();
               $('#calendar').weekCalendar("removeUnsavedEvents");
            },
            buttons: {
               save : function() {

                  calEvent.start = new Date(startField.val());
                  calEvent.end = new Date(endField.val());
                  calEvent.title = titleField.val();
                  calEvent.body = bodyField.val();

                  console.log("Saving event...");

                  $.get('/schedules/update_event/', {title: calEvent.title}, function(data){
                     console.log( data );
                  });

                  calEvent.eventType = typeField.val();

                  $calendar.weekCalendar("updateEvent", calEvent);
                  $dialogContent.dialog("close");
               },
               "delete" : function() {
                  $calendar.weekCalendar("removeEvent", calEvent.id);
                  $dialogContent.dialog("close");
               },
               cancel : function() {
                  $dialogContent.dialog("close");
               }
            }
         }).show();

         var startField = $dialogContent.find("select[name='start']").val(calEvent.start);
         var endField = $dialogContent.find("select[name='end']").val(calEvent.end);
         $dialogContent.find(".date_holder").text($calendar.weekCalendar("formatDate", calEvent.start));
         setupStartAndEndTimeFields(startField, endField, calEvent, $calendar.weekCalendar("getTimeslotTimes", calEvent.start));
         $(window).resize().resize(); //fixes a bug in modal overlay size ??

      },
      eventMouseover : function(calEvent, $event) {
      },
      eventMouseout : function(calEvent, $event) {
      },
      noEvents : function() {

      },
      data : function(start, end, callback) {
         callback(getEventData());
      }
   });

   function resetForm($dialogContent) {
      $dialogContent.find("input").val("");
      $dialogContent.find("textarea").val("");
   }

   function getEventData() {
      var year = new Date().getFullYear();
      var month = new Date().getMonth();
      var day = new Date().getDate();

      return {
         // TODO: fetch json for the saved schedule here
         // [
         //    {"id":1, "start":"2009-05-10T13:15:00.000+10:00", "end":"2009-05-10T14:15:00.000+10:00", "title":"Lunch with Mike"}
         // ]

         events : [
            {
               "id":1,
               "start": new Date(year, month, day - 1, 12),
               "end": new Date(year, month, day - 1, 13, 30),
               "title":"Gospel time!"
            },
            {
               "id":2,
               "start": new Date(year, month, day - 3, 14),
               "end": new Date(year, month, day - 3, 14, 45),
               "title":"Meeting"
            },
            {
               "id":3,
               "start": new Date(year, month, day + 1, 17),
               "end": new Date(year, month, day + 1, 17, 45),
               "title":"Greek"
            },
            {
               "id":4,
               "start": new Date(year, month, day - 1, 8),
               "end": new Date(year, month, day - 1, 9, 30),
               "title":"Team breakfast"
            },
            {
               "id":5,
               "start": new Date(year, month, day - 3, 14),
               "end": new Date(year, month, day - 3, 15),
               "title":"Team time"
            },
            {
               "id":6,
               "start": new Date(year, month, day, 10),
               "end": new Date(year, month, day, 12),
               "title":"I'm read-only - for marking attendance",
               readOnly : true
            }

         ]
      };
   }

   /*
    * Sets up the start and end time fields in the calendar event
    * form for editing based on the calendar event being edited
    */
   function setupStartAndEndTimeFields($startTimeField, $endTimeField, calEvent, timeslotTimes) {

      for (var i = 0; i < timeslotTimes.length; i++) {
         var startTime = timeslotTimes[i].start;
         var endTime = timeslotTimes[i].end;
         var startSelected = "";
         if (startTime.getTime() === calEvent.start.getTime()) {
            startSelected = "selected=\"selected\"";
         }
         var endSelected = "";
         if (endTime.getTime() === calEvent.end.getTime()) {
            endSelected = "selected=\"selected\"";
         }
         $startTimeField.append("<option value=\"" + startTime + "\" " + startSelected + ">" + timeslotTimes[i].startFormatted + "</option>");
         $endTimeField.append("<option value=\"" + endTime + "\" " + endSelected + ">" + timeslotTimes[i].endFormatted + "</option>");

      }
      $endTimeOptions = $endTimeField.find("option");
      $startTimeField.trigger("change");
   }

   var $endTimeField = $("select[name='end']");
   var $endTimeOptions = $endTimeField.find("option");

   // reduces the end time options to be only after the start time options.
   $("select[name='start']").change(function() {
      var startTime = $(this).find(":selected").val();
      var currentEndTime = $endTimeField.find("option:selected").val();
      $endTimeField.html(
            $endTimeOptions.filter(function() {
               return startTime < $(this).val();
            })
            );

      var endTimeSelected = false;
      $endTimeField.find("option").each(function() {
         if ($(this).val() === currentEndTime) {
            $(this).attr("selected", "selected");
            endTimeSelected = true;
            return false;
         }
      });

      if (!endTimeSelected) {
         // automatically select an end date 2 slots away.
         $endTimeField.find("option:eq(1)").attr("selected", "selected");
      }

   });

});