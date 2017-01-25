<?php
	$start = $_GET['start'];
	$len = $_GET['len'];
	$items = array();

	for($i=0;$i<$len;$i++){
		array_push($items,'第'.($start+$i).'行');
	}
	$ret = array('status'=>1,'data'=>$items);
  sleep(1);
	echo json_encode($ret);

?>
