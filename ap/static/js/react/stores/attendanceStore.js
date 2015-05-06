var attendanceStore = Reflux.createStore({
	listenables: [actions],

	getInitialState: function() {
		this.state = {
			events: events,
			rolls: rolls,
			slips: slips,
			date: moment(),
      selectedEvents: {},
      selectedSlips: [],
      weekEvents: []
		};
		return this.state;
	},
	handleDate: function(input) {
    var delta = (input === 'prev') ? -7 : 7;
    this.state.date.add('d', delta);
    this.trigger(this.state);
  },
	onNextWeek: function() {
		this.handleDate('next');
	},
	onPrevWeek: function() {
		this.handleDate('prev');
	},
  onToggleEvent: function(ev) {
  	console.log(ev);
  	console.log(this);
  	console.log(this.state);
    // Add remove selected events based on toggle
    if (!(ev.id in this.state.selectedEvents)) {
      ev.set('selected', 'selected-event');
      this.state.selectedEvents[ev.id] = ev;
    } else {
      ev.set('selected', '');
      delete this.state.selectedEvents[ev.id];
    }
    this.trigger(this.state);

  },
  setRollStatus: function(status) {
    if (_.size(this.state.selectedEvents) <= 0) {
      alert('Please select at 1 event before updating the status');
      return false;
    }
    var key, roll, ev,
        updatedRoll = [];
    var traineeID = parseInt($("input#id_trainee").val());
    // Loop through all the selected events and assign status "status"
    for (key in this.state.selectedEvents) {
      ev = this.state.selectedEvents[key];
      roll = this.props.rolls.get(ev.get('roll'));
      if (!roll) {
        roll = new Roll({
          status: status,
          trainee: traineeID,
          monitor: traineeID,
          event: ev.id
        });
        roll.save();
        this.props.rolls.push(roll);
      } else {
        roll.set('status', status);
        updatedRoll.push(_.pick(roll.attributes, 'id', 'status'));
      }
    }

    // empty selectedEvents
    for (key in this.state.selectedEvents) {
      ev = this.state.selectedEvents[key];
      ev.set('selected', '');
    }

    // unselect all the events
    this.setState({
      selectedEvents: {}
    });

    if (updatedRoll.length > 0) {
      this.props.rolls.sync('patch', new Rolls(updatedRoll), {
        success: function(response, status) {
          console.log('updated status to', status);
        }
      });
    }

  }
})