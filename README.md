# Caminhão

Programa para resolver o problema da maratona descrito em: https://www.beecrowd.com.br/repository/UOJ_1476.html


## 📚 Resumo
O programa tem como objetivo determinar o maior peso bruto que pode ser transportado entre os depósitos e os locais de prova. Para isso ele recebe em um arquivo txt as informações sobre o numero de ilhas(N), pontes(M) e sedes(S). As pontes são descritas em M linhas, contendo as duas ilhas que elas ligam e o peso máximo que suportam, o arquivo termina com S linhas contendo a ilha onde está a sede e a ilha onde está o depósito. Recebendo essas entradas o programa gera um grafo para representar o mapa com os vértices representando as ilhas e as arestas as pontes. Após isso, será gerado outro grafo com a árvore geradora máxima, deixando apenas os caminhos de maior peso no mapa. Com isso uma função irá procurar qual o menor peso entre as sedes e os depósitos, gerando a saída do programa.\
\
As bibliotecas utilizadas foram **networkx** para a geração de grafos e **matplotlib** para a plotagem.

## 🧾 Exemplo
**Entradas:**\
4 5 4\
1 2 9\
1 3 0\
2 3 8\
2 4 7\
3 4 4\
1 4\
2 1\
3 1\
4 3\
**Saída:**\
7\
9\
8\
7


## Autores

- [@gabrielDfavero](https://github.com/gabrielDfavero)

