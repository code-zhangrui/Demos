<div id="stage">
	<canvas id="canvas" width="480" height="600">
		您的浏览器不支持Canvas
	</canvas>
	<div id="rund">
		<div id="core" style="">

		</div>
	</div>
</div>

<script>
let rund = document.getElementById("rund");
let core = document.getElementById("core");

rund.onmousemove = function(e){
	// 首先算出 x 与 y 的比值
	var k = (e.offsetX-core.offsetLeft)/(e.offsetY-core.offsetTop);
	// 然后利用勾股定理，x² + (kx)² = 10²；使得 （1 + k²)x² = 10²，这里 10 是每帧刷新移动的常量
	var newy = Math.sqrt(100/(k*k+1));
	var newx = newy*k;
	console.log(newx, newy);
	//取整
	//加上原值
	//然后处理正负值
	//注意处理圆心问题
}
</script>

<style>
	#stage{
		margin:0px auto;
		width:480px;
		height:700px;
		background:#232323;
	}
	#rund{
		background:red;
		width:90px;
		height:90px;
		border-radius:50px;
		position:relative;
	}
	#core{
		background:white;
		width:1px;
		height:1px;
		position:absolute;
		left:45px;
		top:45px;
	}
</style>
