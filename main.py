import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

## Funções Auxiliares

# Função auxiliar que formata uma linha para evitar repetições nas funções principais.
def formatar():
    print("___________________________________________")

# Função auxiliar que printa a mensagem de operação inválida para evitar repetições nas funções principais.
def invalida():
    print("|\n| Operação Inválida. Tente novamente...")


## Funções Principais

# Função principal que obtém os pontos do quadrilátero do usuário.
def pontos():
    vertices = [] # Inicializa a lista dos vértices
    
    formatar()
    
    for i in range(1,5): # Loop de 1 até 4 para pegar todos os pontos.
      
        coordenadas = input(f"| Coordenadas x e y do ponto {i}: ") # Input da coordenada, uma a uma.

        # Cria o ponto através da lista do split das coordenadas recebidas no input anterior e converte cada coordenada para tipo float.
        ponto = [float(coordenada) for coordenada in coordenadas.split()]
        vertices.append(ponto) # Adiciona o ponto na lista vertices
    
    return vertices

# Função principal que obtém o tipo de transformação desejada.
def tipo_transformacao():
    
    formatar()
    
    # Recebe o tipo da transformação através de um número dentro de uma string.
    tipo = input("| Insira o tipo de transformação: \n| \n| 1) Rotação \n| 2) Cisalhamento \n| 3) Compressão \n| \n| 0) Sair \n| \n| >> ")
    
    # Estrutura de error handler para verificar se o número recebido pelo input é um inteiro e está dentro das alternativas.
    try:
        int(tipo) # Tenta converter o número dentro da string para inteiro.
    except ValueError: 
        invalida() # Printa mensagem de operação inválida se o processo anterior dá errado.
    else:
        
        # Se dá certo, verifica se o inteiro está dentro das opções do programa.
        if int(tipo) > 3 or int(tipo) < 0:
           invalida() # Printa mensagem de erro se não estiver.
        

        else:
            return int(tipo) # Se dá certo, retorna o inteiro que representa o tipo de transformação.

# Função principal que aplica a operação de rotação no quadrilátero dado.
def rotacao():
    vertices = pontos() # Recebe a matriz dos pontos.
    
    angulo = float(input("|\n| Insira o ângulo de rotação em graus: ")) # Input do ângulo de rotação.

    while(angulo == 0): # Restringe para não se possa ter o ângulo de rotação igual a 0.
        invalida() 
        angulo = float(input("|\n| Insira o ângulo de rotação em graus: ")) 


    formatar()

    # Inicializa a lista dos pontos rotacionados a partir dos pontos originais.
    pontos_rotacionados = [] 


    rad = math.radians(angulo) # Converte o ângulo em graus para radianos.
    cos = math.cos(rad) # Cosseno do ângulo em radianos.
    sen = math.sin(rad) # Seno do ângulo em radianos.

    # Matriz de rotação.
    matriz_rotacao = np.array([[cos, -sen],
                               [sen,  cos]])
    
    # Loop para multiplicar a matriz de rotação para cada ponto do quadrilátero.
    for i in range(0,4): 
        coluna = np.transpose(vertices[i]) # Transforma a matriz-linha do ponto em matriz-coluna.

        ponto_rotacionado = np.matmul(matriz_rotacao, coluna) # Multiplica a matriz-coluna pela matriz de rotação.
        pontos_rotacionados.append(ponto_rotacionado) # Adiciona o resultado na lista de pontos rotacionados.

    # Retorna uma lista com os pontos originais e pontos rotacionados para serem usados na função show_polygon.
    return [vertices, pontos_rotacionados] 

# Função principal que aplica a operação de cisalhamento no quadrilátero dado.
def cisalhamento():
    vertices = pontos() # Recebe a matriz dos pontos.

    # Pede os fatores de cisalhamento em x e em y.
    fator_x = float(input("|\n| Insira o fator de cisalhamento em x: ")) 
    fator_y = float(input("| Insira o fator de cisalhamento em y: ")) 

    # Restringe para que não possa ter ambos os fatores iguais a 0 e pede de novo os fatores para o usuário.
    while(fator_x == 0 and fator_y == 0): 
        invalida()
        fator_x = float(input("|\n| Insira o fator de cisalhamento em x: ")) 
        fator_y = float(input("| Insira o fator de cisalhamento em y: "))

    formatar()

    pontos_cisalhados = [] # Inicializa a matriz de pontos cisalhados.

    # Matriz de Cisalhamento.
    matriz_cisalhamento = np.array([[1, fator_x], 
                                    [fator_y, 1]])

    # Loop para multiplicar a matriz de cisalhamento para cada ponto do quadrilátero.
    for i in range(0,4): 
        coluna = np.transpose(vertices[i]) # Transforma a matriz-linha do ponto em matriz-coluna.

        pontos_cisalhado = np.matmul(matriz_cisalhamento, coluna) # Multiplica a matriz-coluna pela matriz de cisalhamento.
        pontos_cisalhados.append(pontos_cisalhado) # Adiciona o ponto cisalhado na lista de pontos cisalhados.

    # Retorna uma lista com os pontos originais e pontos cisalhados para serem usados na função show_polygon.
    return [vertices, pontos_cisalhados]

# Função principal que aplica a operação de compressão no quadrilátero dado.
def compressao():
    vertices = pontos() # Recebe a matriz dos pontos.

    # Pede os fatores de compressão em x e em y.
    fator_x = float(input("|\n| Insira o fator de compressão em x: "))
    fator_y = float(input("| Insira o fator de compressão em y: "))

    # Restringe para que os fatores de compressão não sejam iguais a 1 simultaneamente.
    while(fator_x == 1 and fator_y == 1):
        invalida()
        fator_x = float(input("|\n| Insira o fator de compressão em x: "))
        fator_y = float(input("| Insira o fator de compressão em y: "))
        

    formatar()

    pontos_comprimidos = [] # Inicializa a matriz dos pontos comprimidos.

    # Matriz de Compressão.
    matriz_compressao = np.array([[fator_x, 0],
                                  [0, fator_y]])
    
    # Loop para multiplicar a matriz de compressão para cada ponto do quadrilátero.
    for i in range(0,4):
        coluna = np.transpose(vertices[i]) # Transforma a matriz-linha do ponto em matriz-coluna.

        pontos_comprimido = np.matmul(matriz_compressao, coluna) # Multiplica a matriz-coluna pela matriz de compressão.
        pontos_comprimidos.append(pontos_comprimido) # Adiciona o ponto comprimido na lista de pontos comprimidos.

    # Retorna uma lista com os pontos originais e pontos comprimidos para serem usados na função show_polygon.
    return [vertices, pontos_comprimidos]

# Função principal de plot.
def show_polygon(original_points, transformed_points, title):
    ''' Função que cria dois polígonos a partir dos pontos original_points e transformed_points.
        Entrada:
        list, list, string'''
    # configuração dos tamanhos das fontes das letras e números da figura.
    # para utilizar outros tamanhos, apenas descomentar o tamanho desejado e comentar o não desejado.
    # SMALL_SIZE = 5
    # MEDIUM_SIZE = 10
    BIGGER_SIZE = 15

    plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
    
    # Cria variáveis que vão definir os tamanhos máximos e mínimos da figura, tanto no eixo x quanto no eixo y.
    min_x = min(min(point[0] for point in original_points), min(point[0] for point in transformed_points)) - 1
    min_y = min(min(point[1] for point in original_points), min(point[1] for point in transformed_points)) - 1

    max_x = max(max(point[0] for point in original_points), max(point[0] for point in transformed_points)) + 1
    max_y = max(max(point[1] for point in original_points), max(point[1] for point in transformed_points)) + 1

    fig, ax = plt.subplots()
    # plot do polígono com os pontos original_points
    ax.add_patch(Polygon(original_points, closed=True, fill=None, edgecolor='b', linewidth=2.0))
    # plot do polígono com os pontos transformed_points
    ax.add_patch(Polygon(transformed_points, closed=True, fill=None, edgecolor='r', linewidth=2.0))
    ax.set_title(title, fontsize=20)
    ax.set_xlim([min_x, max_x])
    ax.set_ylim([min_y, max_y])
    ax.set_aspect('equal')
    ax.grid(True)

    # Use plt.show(block=False) para prevenir o block do usuário
    plt.show(block=True)
    
# Função da lógica principal do programa.
def main():
    while(True): # Loop infinito até que se tenha uma quebra pelo break.
        escolha = tipo_transformacao() # Recebe o tipo de transformação.
        
        if escolha == 0: break # Se for 0, quebra o fluxo e vai para a finalização do programa.
        
        elif escolha == 1: # Se for 1, aplica a função de rotação e plota o gráfico.
            pontos = rotacao()
            show_polygon(pontos[0], pontos[1], "Rotação")
        
        elif escolha == 2: # Se for 2, aplica a função de cisalhamento e plota o gráfico.
            pontos = cisalhamento()
            show_polygon(pontos[0], pontos[1], "Cisalhamento")

        elif escolha == 3: # Se for 3, aplica a função de compressão e plota o gráfico.
            pontos = compressao()
            show_polygon(pontos[0], pontos[1], "Compressão")

            

    return "|\n| Programa finalizado.\n"  # Depois de alguma vez digitado o número 0, retorna que o programa foi finalizado.



if __name__ == "__main__":
    print(main())
