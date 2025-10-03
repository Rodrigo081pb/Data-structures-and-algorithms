## Análise dos Problemas e Soluções

Este diretório reúne exercícios e exemplos de estruturas de dados fundamentais, como listas, pilhas, filas, árvores e grafos. Cada problema foi resolvido com foco em clareza e eficiência, utilizando técnicas clássicas da área de algoritmos.

### Complexidade de Tempo

As operações básicas das estruturas de dados foram implementadas buscando o melhor desempenho possível:

- **Listas e Arrays**: Inserção e acesso direto costumam ser rápidos ($O(1)$), mas buscas lineares podem ser mais lentas ($O(n)$).
- **Pilhas e Filas**: Adição e remoção de elementos são feitas em tempo constante ($O(1)$).
- **Árvores Binárias**: Em árvores balanceadas, busca, inserção e remoção geralmente têm complexidade $O(\log n)$; em árvores não balanceadas, podem chegar a $O(n)$.
- **Grafos**: Algoritmos de busca como BFS e DFS percorrem todos os vértices e arestas, com complexidade $O(V + E)$.

### Complexidade de Espaço

O uso de memória depende da estrutura escolhida:

- **Listas, Pilhas e Filas**: Espaço proporcional ao número de elementos ($O(n)$).
- **Árvores**: Espaço $O(n)$ para armazenar todos os nós.
- **Grafos**: Espaço $O(V + E)$ para listas de adjacência; $O(V^2)$ para matriz de adjacência.

### Considerações Finais

As soluções foram pensadas para serem didáticas e eficientes, utilizando a estrutura mais adequada para cada situação. O objetivo é facilitar o entendimento dos conceitos e mostrar como aplicar algoritmos de forma prática e otimizada.
