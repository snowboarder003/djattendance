$(document).ready( function() {

	console.log('According to my earnest expectation and hope that in nothing I will be put to shame, but with all boldness, as always, even now Christ will be magnified in my body, whether through life or through death. Phil. 1:20');

	var mealout = $(".mealout-form");
	var nightout = $(".nightout-form");

	// in case viewing an invalid form or updating; display right away
	var typeselect = $(".leaveslip-form #id_type" );

	// given the leaveslip type, displays or hides the appropriate fields
	function displayType(type) {
		nightout.hide();
	  	mealout.hide();

		switch(type) {
			case "MEAL":
				mealout.show();
				break;
			case "NIGHT":
				nightout.show();
				break;
			default:
				// future options...
				break;
		}
	}

	// triggered upon changing the leaveslip type
	typeselect.change(function() {
		var value = $(this).val();
		displayType(value);
		console.log(value);
	});


})