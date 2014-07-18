var Event = Backbone.Model.extend({
  urlRoot: "/api/event",
  addRoll: function(roll) {
    if(this.get("rolls") === undefined) {
      this.set({
        rolls: new Rolls()
      });
    }
    this.get("rolls").add(roll);
  },
  addSlip: function(slip) {
    this.set('slips', this.get('slips').push(slip.id));
    if(this.status != "approved") {
      this.set("status", slip.get_status_display);
    }
  }
});

var Roll = Backbone.Model.extend({
  urlRoot: "/api/roll"
});

var Leaveslip = Backbone.Model.extend({
  urlRoot: "api/leaveslip"
});
