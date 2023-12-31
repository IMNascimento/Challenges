<div class="header">
<span>beecrowd | 2031</span>
<h1>Pedra, Papel, Ataque Aéreo</h1>
<div>
<p>Por Jeremias Gomes, Universidade de Brasília <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR" /> Brazil</p>
</div>
<strong>Timelimit: 1</strong>
</div>
<div class="problem">
<div class="description">
<p>Pedra, Papel, Ataque Aéreo é um jogo infantil muito popular, em que duas ou mais crianças formam um círculo e fazem gestos com a mão na tentativa de obter a vitória. As regras são surpreendentemente complexas para um jogo de crianças, mas mesmo assim é bastante popular por todo o mundo. </p>
<p>As partidas são muito simples. Os jogadores podem escolher entre o sinal de uma Pedra (o punho), o sinal de um Papel (a palma aberta), e o sinal para o Ataque Aéreo (igual o do Papel, mas com apenas o polegar e o mindinho estendidos). </p>
<p><img alt src="https://resources.beecrowd.com.br/gallery/images/problems/UOJ_2031.png" style="height:200px; width:200px" /></p>
<p>Uma partida, com dois jogadores, possuem as seguintes regras para se definir um vencedor:</p>
<ul>
<li>Ataque Aéreo vs. Pedra: Neste caso, o jogador com o Ataque Aéreo derrota o jogador com a Pedra, por razões óbvias.</li>
<li>Pedra vs. Papel: Neste caso, o jogador com a Pedra derrota o com Papel, porque a Pedra machuca muito mais.</li>
<li>Papel vs. Ataque Aéreo: Aqui o Ataque Aéreo ganha, porque Ataque Aéreo sempre ganha e o Papel é patético.</li>
<li>Papel vs. Papel: Nesta variação, ambos os jogadores ganham, porque o Papel é inútil e ninguém que enfrenta o Papel pode perder.</li>
<li>Pedra vs. Pedra: Para este caso não há ganhador, porque depende do que os jogadores decidem fazer com a Pedra e normalmente não fazem nada.</li>
<li>Ataque Aéreo vs. Ataque Aéreo: Quando isto acontece, todos os jogadores perdem, devido a Aniquilação Mútua.</li>
</ul>
<p>Sua tarefa é escrever um programa que, dada as escolhas de dois jogadores, informe quem venceu o jogo.</p>
</div>
<h2>Entrada</h2>
<div class="input">
<p>A entrada consiste de N (1 ≤ N ≤ 1000) casos de teste. N deve ser lido na primeira linha da entrada. Cada caso de teste é composto por duas linhas, cada uma contendo uma string. A primeira string representa o sinal escolhido pelo jogador 1 e a segunda string representa o sinal escolhido pelo jogador 2. Essas strings podem ser:</p>
<ul>
<li>“ataque”: para representar o Ataque Aéreo</li>
<li>“pedra”: para representar a Pedra</li>
<li>“papel”: para representar o Papel</li>
</ul>
</div>
<h2>Saída</h2>
<div class="output">
<p>A saída deve conter o seguinte:</p>
<ul>
<li>“Jogador 1 venceu”: se o Jogador Um tiver vencido a partida</li>
<li>“Jogador 2 venceu”: se o Jogador Dois tiver vencido a partida</li>
<li>“Ambos venceram”: se os dois jogadores tiverem vencido a partida</li>
<li>“Sem ganhador”: se não houver ganhador</li>
<li>“Aniquilacao mutua”: se ocorrer Aniquilação Mútua</li>
</ul>
<p>Cada saída de um caso de teste deve estar em uma linha. </p>
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
<p>2<br/>
pedra<br/>
pedra<br/>
ataque<br/>
papel</p>
</td>
<td>
<p>Sem ganhador<br/>
Jogador 1 venceu</p>
</td>
</tr>
</tbody>
</table>
<div class="both"></div>
<p class="footer">
Aquecimento da III Maratona de Programação do IFG - Formosa
</p>
</div>

