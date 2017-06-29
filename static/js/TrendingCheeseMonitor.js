var TrendingCheeseMonitor = function() {

	var pollingInterval = 2000;
	var topContainer;

	var init = function() {
		topContainer = $('#trending_cheeses');
		poll();
		setInterval(poll, pollingInterval);
	};

	var poll = function() {
		$.ajax({
			url:'/cheeses',
			dataType:'json',
			success:pollCallback
		});
	};

	var pollCallback = function(response) {
		topContainer.empty();
		$.each(response, function(index, cheese) {
			$('<li>')
				.appendTo(topContainer)
				.text(cheese);
		});
	};

	$(document).ready(init);
};
