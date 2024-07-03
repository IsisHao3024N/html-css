<?php

if( isset($_POST["n1"]) and !empty( $_POST["n1"])){//isset é usado para verificar se a variavel existe
    $n1 = $_POST["n1"];
    $n2 = $_POST["n2"];
    $soma = $n1 + $n2;
    echo $soma;  
}

?>
<form action="" method="POST">
    N1 <input type="text" name="n1"><br>
    N2 <input type="text" name="n2"><br>
    <input type="submit">
</form>