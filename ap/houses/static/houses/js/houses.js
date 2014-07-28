$(document).ready(function() {
    var table = $('#house-table').DataTable();
 
    $('#bunk-submit-changes').click( function() {
        var data = table.$('input, select').serialize();
        alert(
            "The following data would have been submitted to the server: \n\n"+
            data.substr( 0, 120 )+'...'
        );
        return false;
    } );
} );