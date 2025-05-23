<?php
$x = $_POST['x'];
$y = $_POST['y'];
$z = $_POST['z'];
$command = escapeshellcmd("python3 /var/www/html/process_input.py $x $y $z");
$output = shell_exec($command);
echo $output;
?>
