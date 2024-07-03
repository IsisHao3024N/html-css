<?php


if( isset($_POST["nome"]) and !empty( $_POST["nome"])){
    $nome = $_POST["nome"];
    $endereço = $_POST["endereço"];
    $idade = $_POST["idade"];
    $mãe = $_POST["mãe"];
    $pai = $_POST["n2"];
    echo $nome;
    echo $endereço;
    echo $idade;
    echo $mãe;
    echo $pai;

}





?>


<form action="" method="POST">
NOME DO ALUNO(A) <input type="text" name="nomew"><br>
ENDEREÇO <input type="text" name="endereço"><br>
IDADE<input type="text" name="idade"><br>
NOME DA MÃE<input type="text" name="mãe"><br>
NOME DO PAI <input type="text" name="pai"><br>

<input type="submit">
</form>