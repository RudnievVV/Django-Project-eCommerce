// Reset profile image function
jQuery('document').ready(function(){
	jQuery("#reset-image").on("click", function(){
		var image_reset
		image_reset = confirm("Do you confirm image reset?");
		if (image_reset) {
			window.location.replace("/users/my-account/reset-image/")
		} else {
			return false;
		}
	});

});