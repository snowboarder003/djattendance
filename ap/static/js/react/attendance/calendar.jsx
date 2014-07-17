  /** @jsx React.DOM */

  var WeekBar = React.createClass({
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
        <div className="btn-toolbar" role="toolbar">
        <div className="controls btn-group">
        <button className="btn btn-info"><span className="glyphicon glyphicon-calendar"></span></button>
        </div>
        <div className="controls btn-group">
        <button className="btn btn-default clndr-previous-button" onClick={this.prevWeek}>Prev</button>
        <div className="daterange btn btn-default disabled">
        {startdate} to {enddate}
        </div>
        <button className="btn btn-default clndr-next-button" onClick={this.nextWeek}>Next</button>
        </div>
        </div>
        );
    }
  });

  var DaysRow = React.createClass({
    render: function() {
      var days = [];
      for(var i=0;i<7;i++) {
        var name = this.props.date.day(i).format("ddd");
        var num = this.props.date.day(i).format("M/D");
        days.push(
          <div className="col-md-1">
          <div className="schedule-header">
          {name} <br />
          {num}
          </div>
          </div>
          );
      }
      return (
        <div>
        <div className="col-md-1">
        </div>
        {days}
        </div>
        );
    }
  });


  var Event = React.createClass({
    render: function() {
      var ev = this.props.event;
      var classes = "schedule-event " + ev.roll + " " + ev.status;
      var divStyle = {
        top: moment.duration(moment(ev.start).format('H:m')).subtract(6, 'hours').asMinutes()/2,
        height: moment(ev.end).diff(moment(ev.start), 'minutes')/2
      };
      return(
       <div className={classes} style={divStyle} data-id={ev.id} data-roll={ev.roll_id}>
       {ev.code}
       </div>
       );
    }
  });

  var EventGrid = React.createClass({
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
          day_col.push(<Event event={event} key={event.id} />);
        });
        cols.push(<div key={i} className="schedule-header day event col-md-1">{day_col}</div>);
      }
      return (
        <div>
        {cols}
        </div>
        );
    }
  });


  var Time = React.createClass({
    render: function() {
      var hour = moment().hour(this.props.hour).format("h A");
      return(
        <div className="hour">
        {hour}
        </div>

        );
    }
  });

  var TimesColumn = React.createClass({
    render: function() {
      var times = [];
      for(var i=6;i<24;i++) {
        times.push(<Time hour={i} />);
      }
      return (
        <div className="col-md-1 timebar">
        {times}
        </div>
        );
    }
  });


  var Leaveslip = React.createClass({
    render: function() {
      return (
        <div className="panel panel-default" id="submit-leaveslip">
        <div className="panel-heading">
        <h3 className="panel-title" id="event-title">Submit Leave Slip</h3>
        </div>
        <div className="panel-body" id="event-info">
        <form id="leaveslip-form">
        <input type="hidden" id="id_leaveslip" name="leaveslip" value="" />

        <button type="submit" value="creating" className="btn btn-primary">
        Submit
        </button>
        </form>
        </div>
        </div>
        );
    }
  });

  var Roll = React.createClass({
    render: function() {
      return (
        <div className="panel panel-default" id="submit-roll">
        <div className="panel-heading">
        <h3 className="panel-title" id="event-title">Submit Roll</h3>
        </div>
        <div className="panel-body" id="event-info">
        <button id="present" type="button" className="btn btn-default btn-block">Present</button>
        <button id="absent" type="button" className="btn btn-danger btn-block">Absent</button>
        <button id="tardy" type="button" className="btn btn-warning btn-block">Tardy</button>
        <button id="uniform" type="button" className="btn btn-warning btn-block">Uniform</button>
        <button id="left-class" type="button" className="btn btn-warning btn-block">Left Class</button>
        </div>
        </div>
        );
    }
  });

  var Attendance = React.createClass({
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
        <div>
        <WeekBar date={this.state.date} 
        onUserInput={this.handleUserInput}
        />
        <div className="row">
        <DaysRow date={this.state.date} />
        </div>
        <div className="row">
        <TimesColumn />
        <EventGrid events={this.props.events} date={this.state.date} />
        <div className="col-md-4">
        <Roll />
        <Leaveslip />
        </div>
        </div>
        </div>
        );
    }
  });

  React.renderComponent(<Attendance events={events}/>, document.getElementById("react"));
