var moreProducts = [
	{
		img: 'http://img10.360buyimg.com/N3/jfs/t2242/92/1446546284/374195/9196ac66/56af0958N1a723458.jpg',
		name: '珂兰 黄金手 猴哥款',
		price: '￥405.00'
	},{
		img: 'http://img10.360buyimg.com/N3/jfs/t2242/92/1446546284/374195/9196ac66/56af0958N1a723458.jpg',
		name: '珂兰 黄金转运珠 猴哥款',
		price: '￥100.00'
	},{
		img: 'http://img10.360buyimg.com/N3/jfs/t2242/92/1446546284/374195/9196ac66/56af0958N1a723458.jpg',
		name: '珂兰 黄金手链 3D猴哥款',
		price: '￥45.00'
	}
];

function getProductsHtml(products){
	var html = '';
	html += '<li class="products">';
	html += '<div class="cover"><a href="" class="btn">立即抢购</a></div>';
	html += '<a href="#">';
	html += '<img src = "'+products.img+'">';
	html += '<div class="products-name">'+products.name+'</div>';
	html += '<div class="products-price">'+products.price+'</div>';
	html += '</a>';
	html += '</li>';
	return html;
}

$('.btn-add').on('click',function(e){
	e.preventDefault();
	//$('.products-ct').append(getProdHtml(moreProducts[0]));
	//$('.products-ct').append(getProdHtml(moreProducts[1]));
	//$('.products-ct').append(getProdHtml(moreProducts[2]));
	$.each(moreProducts,function(idx,products){
		$('.products-ct').append(getProductsHtml(products));
	})
});
$('.layout').on('mouseenter','.products',function(){
	$(this).addClass('hover');
});
$('.layout').on('mouseleave','.products',function(){
	$(this).removeClass('hover');
});
