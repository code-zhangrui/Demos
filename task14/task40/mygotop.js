var $returnTop = $('<div id="return-top">回到顶部</div>');
		$('body').append($returnTop);

		$(window).on('scroll',function(){
			var top = $(this).scrollTop();
			console.log(top);
			if(top>50){
				$returnTop.show();
			}else {
				$returnTop.hide();
			}
		});
		$returnTop.on('click',function(){
			$(window).scrollTop(0);
		});
