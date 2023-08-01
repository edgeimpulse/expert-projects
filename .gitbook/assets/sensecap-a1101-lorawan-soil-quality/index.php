<?php 
  session_start();
  $Page=0;
?>
<!DOCTYPE html>
<html>
<head>
 <title>Please return to the homepage :) </title>
 
 <?php  include_once $_SERVER['DOCUMENT_ROOT']."/includes/head-start.php"?>
 
  <style>

<?php  include_once $_SERVER['DOCUMENT_ROOT']."/includes/header-style.php"?>
 
 html{background-color:#eb2e00;}
 .divider-p{width:100%;text-align:center;color:white;background-color:transparent;font-family: 'Roboto Slab', serif;font-size:20px;}
</style>

 </head>
 
 <body>
  
<?php ini_set('display_errors',1);?> 
<?php  include_once $_SERVER['DOCUMENT_ROOT']."/includes/header-body.php"?>

<div class="divider" style="height:40px;top:40px;background-color:#1a53ff;"><p class="divider-p">Please return to the home page :) </p></div>

</body>
</html>
  