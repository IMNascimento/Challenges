<div class="header">
<span>beecrowd | 2162</span>
<h1>Picos e Vales</h1>
<div>
<p>Por M.C. Pinto, UNILA <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR" /> Brazil</p>
</div>
<strong>Timelimit: 1</strong>
</div>
<div class="problem">
<div class="description">
<p>Ao observar a paisagem da Nlogônia, o professor MC percebeu que a cada intervalo de 100 metros existe um pico. E que exatamente na metade de dois picos há um vale. Logo, a cada 50 metros há um vale ou um pico e, ao longo da paisagem, não há um pico seguido por outro pico, nem um vale seguido por outro vale.</p>
<p>O professor MC ficou curioso com esse padrão e quer saber se, ao medir outras paisagens, isso se repete. Sua tarefa é, dada uma paisagem, indicar se ela possui esse padrão ou não.</p>
</div>
<h2>Entrada</h2>
<div class="input">
<p>A entrada é dada em duas linhas. A primeira tem o número <strong>N</strong> de medidas da paisagem (1 &lt; <strong>N</strong> ≤ 100). A segunda linha tem <strong>N</strong> inteiros: a altura <strong>H<sub>i</sub></strong> de cada medida (-10000 ≤ <strong>H<sub>i</sub></strong> ≤ 10000, para todo <strong>H<sub>i</sub></strong>, tal que 1 ≤ <strong>i</strong> ≤ <strong>N</strong>). Uma medida é considerada um pico se é maior que a medida anterior. Uma medida é considerada um vale se é menor que a medida anterior.</p>
</div>
<h2>Saída</h2>
<div class="output">
<p>A saída é dada em uma única linha. Caso a paisagem tenha o mesmo padrão da Nlogônia, deve ser mostrado o número 1. Caso contrário, mostra-se o número 0.</p>
</div>
<div class="both"></div>
<table>
<thead>
<tr>
<td>Exemplos de Entrada</td>
<td>Exemplos de Saída</td>
</tr>
</thead>
<tbody>
<tr>
<td class="division">
<p>3<br/>
1 4 -2</p>
</td>
<td>
<p>1</p>
</td>
</tr>
</tbody>
</table>
<div class="both"></div>
<table>
<thead>
</thead>
<tbody>
<tr>
<td class="division">
<p>5<br/>
100 99 112 -8 -7</p>
</td>
<td>
<p>1</p>
</td>
</tr>
</tbody>
</table>
<div class="both"></div>
<table>
<thead>
</thead>
<tbody>
<tr>
<td class="division">
<p>4<br/>
1 2 2 1</p>
</td>
<td>
<p>0</p>
</td>
</tr>
</tbody>
</table>
<p class="footer">
Prova 2 (D1) de Programação de Computadores 2016/1 da UNILA
</p>
