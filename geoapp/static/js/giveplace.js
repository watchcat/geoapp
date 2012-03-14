$(function()
{
	$('label').inFieldLabels();

	var $location = $('#location');

	$location.focus().autocomplete(
		{
			source: function(request, callback)
				{
					$.getJSON('', request.term, function(data)
						{
							var suggestions = [];

							$.each(data, function(i, val)
								{
									suggestions.push(val.name);
								});

							callback(suggestions);
						});
				}
		});

	$('form').submit(function()
		{
			var $result = $('#result');

			$result.empty().addClass('loading').show();

			$.ajax(
				{
					url : '/ajaxmap/' + encodeURIComponent($location.val()),
					dataType : 'html',
					success : function(data)
						{
							$result.fadeOut('fast', function()
									{
										$result
											.removeClass('loading')
											.html(data)
											.fadeIn();
									});
						}
				});

			return false;
		});
});