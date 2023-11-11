<div class="header">
<span>beecrowd | 3042</span>
<h1>Desviando de Árvores de Natal</h1>
<div>
<p>Por Gerson Groth, URI <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR" /> Brazil </p>
</div>
<strong>Timelimit: 1</strong>
</div>
<div class="problem">
<div class="description">
<p>Papai Noel adora jogos de celular, especialmente se forem com temas natalinos. Ele acaba de instalar um novo jogo para seu celular. O jogo consiste em um personagem correndo infinitamente em um caminho composto de três pistas, tendo que trocar de pista para desviar de obstáculos (árvores de natal) que aparecem no caminho. O personagem sempre começa um jogo na pista do meio, sendo necessário que Papai Noel toque uma vez do lado esquerdo da tela do celular para o personagem se deslocar uma pista para a esquerda e um toque do lado direito da tela para se deslocar uma pista para o lado direito. Ou seja, se o personagem estiver na pista mais à esquerda, precisará de 2 toques do lado direito para chegar até a pista mais à direita.<br/>
Apesar de parecer simples, Papai Noel está tendo dificuldades em permanecer vivo por muito tempo. Uma coisa que ele notou durante o jogo é que, sempre que há obstáculos, somente uma das pistas está livre para atravessar, enquanto que as outras duas possuem árvores de natal bloqueando os caminhos. Como vocês são grandes amigos, ele pediu sua ajuda para escrever um programa que minimize o número de toques necessários na tela para que ele consiga percorrer M metros no jogo.</p>
</div>
<h2>Entrada</h2>
<div class="input">
<p>A entrada consiste de vários casos de teste. A primeira linha de um caso de teste contém um inteiro <strong>M</strong> (0 ≤ <strong>M</strong> &lt; 10000), representando a distância, em metros, que Papai Noel deseja jogar. As próxima <strong>M</strong> linhas contém, cada uma, 3 inteiros <strong>L</strong>,<strong>C</strong>,<strong>R</strong> representando a pista da esquerda, centro e direita, respectivamente (0 ≤ <strong>L,C,R</strong> ≤ 1). As pistas contém apenas o número 0, caso não tenha nenhum obstáculo, e o número 1, caso haja uma árvore de natal na pista. É garantido que ao menos uma pista sempre estará livre para o personagem passar. Assuma que Papai Noel sempre consegue tocar rápido o suficiente na tela para sair da esquerda até a direita, ou da direita até a esquerda de uma entrada até a outra. O final da entrada é indicado por uma linha que contém apenas um zero.</p>
</div>
<h2>Saída</h2>
<div class="output">
<p>Para cada caso de teste, seu programa deve imprimir uma única linha contendo o menor número de toques na tela que Papai Noel deve fazer para percorrer a distância desejada desviando de todos os obstáculos.</p>
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
<p>5<br/>
0 0 0<br/>
1 1 0<br/>
0 0 0<br/>
0 0 0<br/>
1 0 1<br/>
0</p>
</td>
<td>
<p>2</p>
</td>
</tr>
</tbody>
</table>
<div class="both"></div>
<p class="footer">
</p>
</div>
