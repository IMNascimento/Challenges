<div class="header">
<span>beecrowd | 1252</span>
<h1>Sort! Sort!! e Sort!!!</h1>
<div><p>
Por Shahriar Manzoor, <img alt src="https://resources.beecrowd.com.br/gallery/images/flags/bd.gif" style="width: 16px; height: 11px; "/> Bangladesh</p>
</div>
<strong>Timelimit: 2</strong>
</div>
<div class="problem">
<div class="description">
<p>
Hmm! Aqui você foi solicitado a fazer uma simples ordenação. A você serão dado <strong>N </strong>números
e um inteiro positivo <strong>M</strong>. Você terá que ordenar estes <strong>N </strong>números em ordem
ascendente de seu módulo <strong>M</strong>. Se houver um empate entre um número ímpar e um número par
(para os quais o seu módulo <strong>M </strong>dá o mesmo valor) então o número impar irá preceder o número par.
Se houver um empate entre dois números ímpares (para os quais o seu módulo <strong>M</strong> dá o
mesmo valor), então o maior número ímpar irá preceder o menor número ímpar. Se houve um empate entre dois números
pares (para os quais o seu módulo <strong>M</strong> dá o mesmo valor), então o menor número par irá
preceder o maior número par. Para o resto de valores negativos siga a regra de linguagem de programação
C: um número negativo nunca pode ter módulo maior do que zero. Por exemplo,&nbsp;-100 MOD 3 = -1, -100 MOD 4 = 0, etc.</p>
</div>
<h2>Entrada</h2>
<div class="input">
<p>
A entrada contém vários casos de teste. Cada caso de teste inicia com dois inteiros &nbsp;<strong>N </strong>(0 &lt; <strong>N </strong>≤ 10000) e <strong>M</strong> (0 &lt; <strong>M </strong>≤ 10000) que denotam quantos números existirão neste conjunto. Cada uma das próximas <strong>N</strong> linhas conterá um número cada. Estes números deverão caber em um inteiro de 32 bits com sinal. A entrada é terminada por uma linha que conterá dois valores nulos (0) e não deve ser processada.</p>
</div>
<h2>Saída</h2>
<div class="output">
<p>
A primeira linha de cada conjunto de saída irá contér os valores de <strong>N</strong> e <strong>M</strong>. As próximas <strong>N</strong> linhas irão contér <strong>N</strong> números, ordenados de acordo com as regras acima mencionadas. Imprima os dois últimos zeros da entrada para a saída padrão.</p>
</div>
<div class="both"></div>
<table>
<thead>
<tr>
<td>Exemplo de Entrada</td>
<td>Exemplo de Saída</td>
</tr>
</thead>
<tbody>
<tr>
<td class="division">
<p>
15 3<br/>
1<br/>
2<br/>
3<br/>
4<br/>
5<br/>
6<br/>
7<br/>
8<br/>
9<br/>
10<br/>
11<br/>
12<br/>
13<br/>
14<br/>
15<br/>
3 3<br/>
9<br/>
12<br/>
10<br/>
0 0</p>
</td>
<td>
<p>
15 3<br/>
15<br/>
9<br/>
3<br/>
6<br/>
12<br/>
13<br/>
7<br/>
1<br/>
4<br/>
10<br/>
11<br/>
5<br/>
2<br/>
8<br/>
14<br/>
3 3<br/>
9<br/>
12<br/>
10<br/>
0 0</p>
</td>
</tr>
</tbody>
</table>
<p class="footer">
Agradecimento especial a Syed Monowar Hossain. Tradução, entrada e saída por Neilor.</p>
</div>
