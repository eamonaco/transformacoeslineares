# Transformações Geométricas em 2D com Python

- O zip contém o código `main.py` que realiza transformações geométricas em polígonos 2D, usando conceitos de Transformações Lineares da Álgebra Linear. As transformações suportadas são rotação, cisalhamento e compressão. O programa utiliza a biblioteca NumPy para manipulação de matrizes e a biblioteca Matplotlib para exibição dos polígonos antes e depois da transformação.

- O código também possui a opção de sair a qualquer momento, digitando o número 0.


## Funções Auxiliares

### `formatar()`

- Função auxiliar que imprime uma linha para formatar a GUI (Interface Gráfica do Usuário).

### `invalida()`

- Função que imprime uma mensagem indicando que a operação é inválida e pede para tentar novamente. É usada para aplicar a restrições nas funções principais


## Funções Principais

### `pontos()`

- Função que solicita ao usuário inserir as coordenadas de quatro pontos no plano 2D e retorna uma lista de vértices. Esses vértices são usados dentro das funções que aplicam as transformações, para facilitar a leitura do código.

### `tipo_transformacao()`

- Função que solicita ao usuário inserir o tipo de transformação desejada (rotação, cisalhamento, compressão) e retorna a escolha como um inteiro. Esse inteiro controlará o fluxo do programa.

### `rotacao()`

- Função que realiza a rotação dos pontos em torno da origem com base no ângulo fornecido pelo usuário.

### `cisalhamento()`

- Função que realiza o cisalhamento dos pontos nas direções x e y com base nos fatores fornecidos pelo usuário.

### `compressao()`

- Função que realiza a compressão dos pontos nas direções x e y com base nos fatores fornecidos pelo usuário.

### `show_polygon(original_points, transformed_points, title)`

- Função que exibe dois polígonos a partir dos pontos originais e transformados com um título, indicando o tipo de transformação.

### `main()`

- Função principal que implementa o menu para escolher o tipo de transformação e chama as funções correspondentes. Também pode ser considerada como a função que aplica a GUI.

## Execução

#### Linux

- Entre no terminal, vá até o diretório do arquivo e digite:
	`python3 main.py`

#### Windows

- O código pode ser rodado em uma IDE especializada (IDLE, Pycharm, Google Colab, VSCode).

## Dependências

- python 3.10
- numpy
- matplotlib
- math
- python-tk
