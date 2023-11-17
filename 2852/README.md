<div class="header">
<span>beecrowd | 2852</span>
<h1>Troca de Mensagens</h1>
<div>
<p>Por Jessica Dagostini, beecrowd <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR" /> Brazil</p>
</div>
<strong>Timelimit: 1</strong>
</div>
<div class="problem">
<div class="description">
<p>João e Enzo adoram criptografar as suas mensagens. Para essa criptografia, eles utilizam a técnica da cifra de Vigenère. Essa técnica é bastante semelhante a cifra de Cesar, porém utiliza de diversas "chaves" para cada letra da frase a ser criptografada. A tabela abaixo demonstra o padrão da cifra, consistindo na repetição do alfabeto 26 vezes, onde em cada linha uma letra é deslocada para a esquerda em relação a linha anterior. Essas 26 linhas correspondem às 26 possíveis cifras de César.</p>
<p class="center"><img src="https://resources.beecrowd.com.br/gallery/images/contests/UOJ_383_K.png" alt style="width: 400px" /></p>
<p>Uma palavra aleatória é escolhida como palavra-chave, e cada letra desta palavra vai indicar a linha a ser utilizada para cifrar ou decifrar uma letra da mensagem. Por exemplo:</p>
<ul>
<li>O texto a ser criptografado é "ciencia da computacao";</li>
<li>Definimos como palavra-chave "obi";</li>
<li>Agora, devemos repetir a palavra-chave tantas vezes forem necessárias até obtermos o comprimento do texto a ser criptografado:
<ul>
<li>ciencia da computacao</li>
<li>obiobio bi obiobiobio</li>
</ul>
</li>
<li>Para realizar a criptografia da primeira letra, devemos encontrar a linha da letra "o" na tabela, e procurar pela coluna da primeira letra da palavra, "c". Para a segunda letra, devemos procurar pela linha "b" coluna "i", e assim por diante, até termos como resultado:
<ul>
<li>qjmbdqo ei qpudvbodic</li>
</ul>
</li>
</ul>
<p>Uma vez que realizar a cifragem de todas as palavras das mensagens a serem enviadas é um trabalho bastante custoso, os amigos decidiram que somente irão criptografar as palavras que iniciarem com uma letra consoante. Sendo assim, eles <i>somente aplicarão a palavra-chave nas palavras que eles irão de fato criptografar</i>.</p>
<p>Dada uma palavra-chave e um texto de uma mensagem, sua tarefa é criptografar esta mensagem utilizando a cifra de Vigenère mas não esquecendo da regra adicionada por João e Enzo.</p>
</div>
<h2>Entrada</h2>
<div class="input">
<p>A primeira linha contém uma palavra-chave <strong>K</strong> (3 &le; <strong>K</strong> &le; 45), que representa a chave para a criptografia. Ela somente é formada pelo alfabeto (a-z) em letras minúsculas, sem espaços. A linha a seguir contém um inteiro <strong>N</strong>&nbsp;(1 &le; <strong>N</strong> &le; 150) que indica a quantidade de mensagens a serem criptografadas. As próximas&nbsp;<strong>N</strong>&nbsp;linhas correspondem as mensagens. Estas mensagens não ultrapassam 10<sup>5</sup>&nbsp;caracteres e são compostas pelo alfabeto (a-z) em letras minúsculas e por espaços.</p>
</div>
<h2>Saída</h2>
<div class="output">
<p>A saída deve apresentar a mensagem criptografada, de acordo com a regra dos amigos.</p>
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
obi<br/>
2<br/>
olimpiada brasileira de informatica<br/>
ciencia da computacao<br/>
</td>
<td>
olimpiada psigjtsjzo em informatica<br>
qjmbdqo ei qpudvbodic<br/>
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
informatica<br/>
2<br/>
ciencia da computacao<br/>
olimpiada brasileira de informatica<br/>
</td>
<td>
kvjbtua wi eouczhroah<br/>
olimpiada jefgzxebzc dm informatica<br/>
</td>
</tr>
</tbody>
</table>
<p class="footer">
Aquecimento da OBI - Fase Nacional 2018
</p>
</div>
