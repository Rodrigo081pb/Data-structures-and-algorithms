## Task0

**Descrição**: Imprime o primeiro registro de textos e o último de chamadas.
**Abordagem**: Acessa diretamente o primeiro e último elemento das listas.
**Complexidade**:
- **Algoritmo**: Operação de acesso direto em lista.
- **Big O**: $O(1)$
- **Justificativa**: O acesso a elementos por índice em listas é constante.


## Task1

**Descrição**: Conta o número de telefones distintos nos registros de textos e chamadas.
**Abordagem**: Itera sobre todos os registros e adiciona os números em um conjunto.
**Complexidade**:
- **Algoritmo**: Iteração sobre todos os registros.
- **Big O**: $O(n)$
- **Justificativa**: Cada registro é acessado uma vez; inserção em conjunto é $O(1)$.


## Task2

**Descrição**: Encontra o número de telefone que mais tempo passou em chamadas.
**Abordagem**: Itera sobre todas as chamadas, somando o tempo para cada número.
**Complexidade**:
- **Algoritmo**: Iteração sobre todos os registros de chamadas.
- **Big O**: $O(n)$
- **Justificativa**: Cada chamada é processada uma vez; operações de dicionário são $O(1)$.


## Task3

**Descrição**: Encontra os códigos chamados por Bangalore e calcula a porcentagem de chamadas para Bangalore.
**Abordagem**: Itera sobre as chamadas, verifica prefixos e conta ocorrências.
**Complexidade**:
- **Algoritmo**: Iteração sobre todos os registros de chamadas, ordenação dos códigos.
- **Big O**: $O(n + k \log k)$
- **Justificativa**: $O(n)$ para iterar e coletar códigos, $O(k \log k)$ para ordenar os códigos únicos ($k$ = quantidade de códigos únicos).


## Task4

**Descrição**: Identifica possíveis números de telemarketing.
**Abordagem**: Cria conjuntos de números e faz operações de diferença.
**Complexidade**:
- **Algoritmo**: Iteração sobre todos os registros e operações de conjunto.
- **Big O**: $O(n)$
- **Justificativa**: Cada registro é acessado uma vez; operações de conjunto são eficientes.


