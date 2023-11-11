<?php

// Dicionário que mapeia a soma dos botões para a música correspondente
$musicas = array(
    0 => "PROXYCITY",
    1 => "P.Y.N.G.",
    2 => "DNSUEY!",
    3 => "SERVERS",
    4 => "HOST!",
    5 => "CRIPTONIZE",
    6 => "OFFLINE DAY",
    7 => "SALT",
    8 => "ANSWER!",
    9 => "RAR?",
    10 => "WIFI ANTENNAS"
);

// Número de casos de teste
$C = intval(fgets(STDIN));

for ($i = 0; $i < $C; $i++) {
    // Ler os botões pressionados (X e Y)
    $input = explode(" ", trim(fgets(STDIN)));
    $X = intval($input[0]);
    $Y = intval($input[1]);

    // Calcular a soma dos botões e imprimir a música correspondente
    $soma = $X + $Y;
    echo $musicas[$soma] . "\n";
}

?>