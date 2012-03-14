$(function()
{
	$('label').inFieldLabels();

	var $location = $('#location');

	$location.focus().autocomplete(
		{
			source: function(request, callback)
				{
					$.getJSON('/autocomplete/' + encodeURIComponent(request.term), function(data)
						{
							var suggestions = [];

							$.each(data.predictions, function(i, val)
								{
									suggestions.push(val.description);
								});

							callback(suggestions);
						});
				}
		});

	$('form').submit(function()
		{
			var $result = $('#result'),
				$loading = $('#loading');

			$result.stop().hide();
			$loading.show();

			$.ajax(
				{
					url : '/ajaxmap/' + encodeURIComponent($location.val()),
					dataType : 'html',
					success : function(data)
						{
							$loading.hide();
							$result.empty();

							var ifrm = $result[0];
							ifrm = (ifrm.contentWindow) ? ifrm.contentWindow : (ifrm.contentDocument.document) ? ifrm.contentDocument.document : ifrm.contentDocument;
							ifrm.document.open();
							ifrm.document.write(data);
							ifrm.document.close();

							$result.fadeIn();
						}
				});

			return false;
		});
});