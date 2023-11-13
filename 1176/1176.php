<?php

$fibonacci = [0, 1];

for ($i = 2; $i < 62; $i++) {
    $calc = $fibonacci[$i - 1] + $fibonacci[$i - 2];
    $fibonacci[] = $calc;
}

$teste = intval(fgets(STDIN));

for ($j = 1; $j <= $teste; $j++) {
    $n = intval(fgets(STDIN));
    echo "Fib($n) = {$fibonacci[$n]}\n";
}

?>