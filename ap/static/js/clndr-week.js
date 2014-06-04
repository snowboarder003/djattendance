function weeksInMonth(month) {
    return Math.floor((month.daysInMonth() + moment(month).startOf('month').weekday()) / 7);
}

var clndr = $('#clndr').clndr({
    template: $('#clndr-template').html(),

    extras: {
        currentWeek: Math.floor( ( ( (moment().date() + moment().startOf('month').weekday() ) - 1 ) / ( weeksInMonth(moment() ) * 7) ) * weeksInMonth( moment() ) ),
    },

    daysOfTheWeek: ['LD', 'Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat'],

    doneRendering: function() {
        /* Next button handler */
        $('#clndr .clndr-next-button').on('click', function() {
            /* Get numbers of weeks in the month */
            var weeks_in_month = Math.floor(clndr.month.daysInMonth() / 7) - 1;
            if(clndr.options.extras.currentWeek < weeks_in_month) {
                /* Increase the week count */
                clndr.options.extras.currentWeek += 1;
            } else {
                /* Reset the week count */
                clndr.options.extras.currentWeek = 0;
                /* Go to next month */
                clndr.next();
            }
            clndr.render();
        });

        /* Previous button handler */
        $('#clndr .clndr-previous-button').on('click', function() {
            /* Get numbers of weeks in the month */
            var weeks_in_month = Math.floor(clndr.month.daysInMonth() / 7) - 1;
            if(clndr.options.extras.currentWeek > 0) {
                /* Decrease the week count */
                clndr.options.extras.currentWeek -= 1;
            } else {
                /* Reset the week count */
                clndr.options.extras.currentWeek = weeks_in_month;
                /* Go to previous month */
                clndr.back();
            }
            clndr.render();
        });
    }
});
