<?php
if ( isset($_POST["linhas"]) and !empty( $_POST["linhas"])){
    $linhas = ($_POST["linhas"]);
    $coluna = ($_POST["coluna"]);  


echo "<table border='1'>";
for($i = 1;$i <= $linhas;$i++){
    echo"<tr>";
    if($i == 1){
        echo"<tr colspan='3'>";
    } 
        for($j = 1; $j <= $coluna; $j++){
            echo"<td>";
            echo"linha $i coluna $j";
            echo"</td>";
            }
    echo"</tr>";
}
echo"</table>";
}
?>
<form action="" method="POST">
    linhas <input type="text" name="linhas"><br>
    coluna <input type="text" name="coluna"><br>
    <input type="submit">
</form>