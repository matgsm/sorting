Programa pode trabalhar com listas sempre ordenadas ou segundo escolha do usuario. Para isso basta editar main.py, linha 10:

ALWAYS_ORDERED = True	#trabalha apenas com listas ordenadas
ALWAYS_ORDERED = False  #trabalha com qualquer tipo de listas

Caso se esteja trabalhando com qualquer tipo de lista, o programa "pergunta" ao usuario se a lista está ordenada logo após a seleção de listas. Caso a lista não esteja ordenada ou o usuario não saiba, quando for solicitado ao programa fazer Pesquisa Binaria o programa primeiro faz automaticamente a ordenação usando Merge_Sort e em seguida o usuario pode fazer quantas buscas quiser.

Novas listas podem ser adicionados pela pasta ./logs
O programa os detecta automaticamente e os lista entre as opções para o usuario escolher.

1) O arquivo use_list.py contem as estruturas necessarias para a seleção e leitura de listas contidas em ./logs 

2) O arquivo sorting.py contem as estruturas de dados dos metodos de ordenação.

3) O arquivo search.py contem as estruturas de dados dos metodos de busca.

4) O arquivo menu.py contem as estruturas de dados necessárias para gerar os menus interativos, bem como o metodo do menu principal: interface()

5) O arquivo monitor.py contem as estruturas necessarias para o monitoramento dos metodos de ordenação e busca, tais como analise de tempo, contagem de comparações e indice de elementos encontrados na busca

6) O arquivo use_sorting.py cria o menu para seleção do metodo de ordenação usando estruturas de menu.py e, segundo a alternativa escolhida, usa as estruturas contidas em sorting.py para ordenar a lista

7) O arquivo use_search.py cria o menu para selação do metodo de busca usando estruturas de menu.py e, segundo a alternativa escolhida, usa as estruturas contidas em search.py para fazer a busca em uma copia da lista.
Obs: Se escolhido busca binaria para uma lista não ordenada, desde que ALWAYS_ORDERED esteja definido como falso, o programa faz uso das informações obtidas junto ao usuario durante a seleção da lista e, se a lista nao estiver ordenada, ou o usuario não souber, o programa ordena automaticamente usando merge_sort antes de fazer a busca binaria. Infelizmente o metodo merge_sort é consideravelmente mais lento do que a busca binaria, mas apresenta uma eficiencia boa e principalmente constante para listas ordenadas de qualquer maneira (crescente, decrescente ou aleatorias) O(n)= nlogn.

8) O arquivo main.py faz a integração de todas as funções, tendo sua execução em torno de um loop para encerrar o programa apenas quando definido pelo usuario, com opções para ordenar a lista, fazer buscas, imprimir a lista e escolher novas listas.
  
Para executar o programa basta executar o arquivo main.py
	em linux:
	python main.py
