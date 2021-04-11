
<html>
<body>
<p>hello</p>
</body>
</html>

<?php
$url = 'http://localhost:5000/events';

//Use file_get_contents to GET the URL in question.
$contents = file_get_contents($url);

//If $contents is not a boolean FALSE value.
if($contents !== false){
    //Print out the contents.
    // echo $contents;
    $contents=json_decode($contents)
    echo $contents->_id;
}
?>