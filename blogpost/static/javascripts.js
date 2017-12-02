

var $search = $('span'),
    $input   = $('#search_input'),
    visible = false,
    $nav = $('nav ul');

 	$('#search_input').hide();

// $(document).load(function(){
// 	console.log("helloooo");
// });

$search.hover(
	function(){
		console.log("ive been hovered");
		if (visible) {
			console.log("im true!");
			$input.on("focus", function(){
				console.log("im a focus");
				// $(this).css("background-color", "pink");
			}).mouseleave(function(){
				$(this).fadeOut('slow', function(){
					console.log("im a mouseout");
				});
				// $nav.addClass('smooth');
				// $()
			});
			visible = false;
		
		} else {
			console.log("helloooo it's false");
			$input.show(300, function(){
				$(this).addClass('input_style');
				console.log('whattttt', $(this));
				console.log("complete");
			});
			console.log("we skipped stuff");
			visible = true;
			
		}

});







