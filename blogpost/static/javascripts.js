var $search = $('#searchIcon'),
    $input   = $('#search_input'),
    visible = false,
    $nav = $('nav ul');
    $side = $('#mySidenav');
    $open = $('#open');
    $close = $('#close');

 $('#search_input').hide();

$search.hover(
	function(){
		if (visible) {
			$input.on("focus", function(){
			}).mouseleave(function(){
				$(this).fadeOut('slow', function(){
				});
			});
			visible = false;
		} else {
			$input.show(300, function(){
				$(this).addClass('input_style');
			});
			visible = true;
		}
});

$open.click(
	function openNav() {
		$side.css("width", "250px");
	}
);

$close.click(
	function closeNav(){
		$side.css("width", "0");
	});






