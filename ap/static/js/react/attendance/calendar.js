  /** @jsx React.DOM */

  var WeekBar = React.createClass({displayName: 'WeekBar',
    nextWeek: function() {
      this.props.onUserInput("next");
    },
    prevWeek: function() {
      this.props.onUserInput("prev");
    },
    render: function() {
      var startdate = this.props.date.weekday(0).format("M/D/YY");
      var enddate = this.props.date.weekday(6).format("M/D/YY");
      return (
        React.DOM.div( {className:"btn-toolbar", role:"toolbar"}, 
        React.DOM.div( {className:"controls btn-group"}, 
        React.DOM.button( {className:"btn btn-info"}, React.DOM.span( {className:"glyphicon glyphicon-calendar"}))
        ),
        React.DOM.div( {className:"controls btn-group"}, 
        React.DOM.button( {className:"btn btn-default clndr-previous-button", onClick:this.prevWeek}, "Prev"),
        React.DOM.div( {className:"daterange btn btn-default disabled"}, 
        startdate, " to ", enddate
        ),
        React.DOM.button( {className:"btn btn-default clndr-next-button", onClick:this.nextWeek}, "Next")
        )
        )
        );
    }
  });

  var DaysRow = React.createClass({displayName: 'DaysRow',
    render: function() {
      var days = [];
      for(var i=0;i<7;i++) {
        var name = this.props.date.day(i).format("ddd");
        var num = this.props.date.day(i).format("M/D");
        days.push(
          React.DOM.div( {className:"col-md-1"}, 
          React.DOM.div( {className:"schedule-header"}, 
          name, " ", React.DOM.br(null ),
          num
          )
          )
          );
      }
      return (
        React.DOM.div(null, 
        React.DOM.div( {className:"col-md-1"}
        ),
        days
        )
        );
    }
  });


  var Event = React.createClass({displayName: 'Event',
    render: function() {
      var ev = this.props.event;
      var classes = "schedule-event " + ev.roll + " " + ev.status;
      var divStyle = {
        top: moment.duration(moment(ev.start).format('H:m')).subtract(6, 'hours').asMinutes()/2,
        height: moment(ev.end).diff(moment(ev.start), 'minutes')/2
      };
      return(
       React.DOM.div( {className:classes, style:divStyle, 'data-id':ev.id, 'data-roll':ev.roll_id}, 
       ev.code
       )
       );
    }
  });

  var EventGrid = React.createClass({displayName: 'EventGrid',
    render: function() {
      var cols = [];
      //get events only from the state's week
      var week_events = _.filter(this.props.events, function(ev) {
        return (this.props.date.weekday(0) < moment(ev.start) && this.props.date.weekday(6) > moment(ev.end));
      }, this);
      
      for(var i=0;i<7;i++) {
        //get events for one day
        var day_events = _.filter(week_events, function(ev) {
          return moment(ev.start).weekday() === i; // this == i
        });

        var day_col = [];
        day_events.forEach(function(event) {
          day_col.push(Event( {event:event, key:event.id} ));
        });
        cols.push(React.DOM.div( {key:i, className:"schedule-header day event col-md-1"}, day_col));
      }
      return (
        React.DOM.div(null, 
        cols
        )
        );
    }
  });


  var Time = React.createClass({displayName: 'Time',
    render: function() {
      var hour = moment().hour(this.props.hour).format("h A");
      return(
        React.DOM.div( {className:"hour"}, 
        hour
        )
        );
    }
  });

  var TimesColumn = React.createClass({displayName: 'TimesColumn',
    render: function() {
      var times = [];
      for(var i=6;i<24;i++) {
        times.push(Time( {hour:i} ));
      }
      return (
        React.DOM.div( {className:"col-md-1 timebar"}, 
        times
        )
        );
    }
  });


  var Leaveslip = React.createClass({displayName: 'Leaveslip',
    render: function() {
      return (
        React.DOM.div( {className:"panel panel-default", id:"submit-leaveslip"}, 
        React.DOM.div( {className:"panel-heading"}, 
        React.DOM.h3( {className:"panel-title", id:"event-title"}, "Submit Leave Slip")
        ),
        React.DOM.div( {className:"panel-body", id:"event-info"}, 
        React.DOM.form( {id:"leaveslip-form"}, 
        React.DOM.input( {type:"hidden", id:"id_leaveslip", name:"leaveslip", value:""} ),

        React.DOM.button( {type:"submit", value:"creating", className:"btn btn-primary"}, 
        "Submit"
        )
        )
        )
        )
        );
    }
  });

  var Roll = React.createClass({displayName: 'Roll',
    render: function() {
      return (
        React.DOM.div( {className:"panel panel-default", id:"submit-roll"}, 
        React.DOM.div( {className:"panel-heading"}, 
        React.DOM.h3( {className:"panel-title", id:"event-title"}, "Submit Roll")
        ),
        React.DOM.div( {className:"panel-body", id:"event-info"}, 
        React.DOM.button( {id:"present", type:"button", className:"btn btn-default btn-block"}, "Present"),
        React.DOM.button( {id:"absent", type:"button", className:"btn btn-danger btn-block"}, "Absent"),
        React.DOM.button( {id:"tardy", type:"button", className:"btn btn-warning btn-block"}, "Tardy"),
        React.DOM.button( {id:"uniform", type:"button", className:"btn btn-warning btn-block"}, "Uniform"),
        React.DOM.button( {id:"left-class", type:"button", className:"btn btn-warning btn-block"}, "Left Class")
        )
        )
        );
    }
  });

  var Attendance = React.createClass({displayName: 'Attendance',
    handleUserInput: function(input) {
      if(input==="next") {
        this.setState({
          date: this.state.date.add("d", 7)
        });
      } else if(input==="prev") {
        this.setState({
          date: this.state.date.add("d", -7)
        });
      }
    },
    getInitialState: function() {
      return {
        date: moment()
      };
    },
    render: function() {
      return (
        React.DOM.div(null, 
        WeekBar( {date:this.state.date, 
        onUserInput:this.handleUserInput}
        ),
        React.DOM.div( {className:"row"}, 
        DaysRow( {date:this.state.date} )
        ),
        React.DOM.div( {className:"row"}, 
        TimesColumn(null ),
        EventGrid( {events:this.props.events, date:this.state.date} ),
        React.DOM.div( {className:"col-md-4"}, 
        Roll(null ),
        Leaveslip(null )
        )
        )
        )
        );
    }
  });

  React.renderComponent(Attendance( {events:events}), document.getElementById("react"));

  console.log("this is a new edit");
