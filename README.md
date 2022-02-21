

# Caixeiro Viajante Carioca

**Número da Lista**: 2 <br>
**Conteúdo da Disciplina**: Grafos 2

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0164357  |  Ugor Brandão |
| 17/0161897 | Eduarda Servidio |

## Sobre  
Fizemos duas experiências para o usuário, uma para o usuário interagir manualmente com as distâncias entre os pontos. E uma experiência automática, trazendo a variável de preços (simulando valores de uma corrida com aplicativo de transporte privado), que mostra o caminho com menor preço.

### Experiência Manual
Você está no Rio de Janeiro e quer encontrar o menor caminho para percorrer os pontos turísticos! Você tem acesso a um mapa onde mostra todos os pontos turísticos do RJ. Cada caminho possui uma cor. Caminhe através dos botões e suas respectivas cores e saiba qual o menor caminho para percorrer os pontos.

### Experiência Automática
Você está no Rio de Janeiro e quer visitar todos os pontos turísticos gastando o menor valor! Você tem acesso a um mapa onde mostra todos os pontos turísticos do RJ. Cada caminho possui uma cor. Jogue e encontre os caminhos que te levam a gastar o menor valor. <br> Foi utilizado o algoritmo de Prim para encontrar os caminhos que no final totalizam o menor valor gasto.

## Screenshots
### Experiência Manual
![image](https://user-images.githubusercontent.com/52542729/154977138-6d7341b9-6119-4f84-96c2-ff86e8dc39a9.png)
Figura 1: Tela Inicial

![image](https://user-images.githubusercontent.com/52542729/154977350-6631ab17-5cfc-4c3d-b63b-e09ea2c8b823.png)
Figura 2: Tela do jogo quando o usuário apertar algum botão.<br>

Na figura 2, a aresta referente a cor do botão que o usuário apertou ficará vermelha e aparecerá quantos Km ele percorreu.

### Experiência Automática
![image](https://user-images.githubusercontent.com/52542729/154973454-1409e85d-6a45-4a02-9f22-55d3ecf43af7.png)
Figura 3: Tela do jogo. <br>

Na figura 3, ao clicar em jogar, aparecerá o menor valor para visitar os pontos turísticos.

## Instalação 
**Linguagem Experiência Manual**: HTML e JavaScript. <br>
**Linguagem Experiência Automática**:HTML, CSS e Python. <br>
**Pré-requisitos**: ter o Python e o Flask instalados na máquina, abrir e executar os arquivos de preferência no VSCode. Ao executar o arquivo HTML, um localhost será criado, dando acesso ao jogo.

## Uso
### Experiência Manual
O usuário deve utilizar os botões coloridos. Cada botão tem sua aresta de mesma cor. Ao clicar no botão, a aresta correspondente ficará vermelha e o total de km percorridos aparecerá. O jogo reinicia quando o jogador alcançar 76 km que é o tamanho menor entre os pontos turísticos, se ele ultrapassar a mensagem que o jogador perdeu aparecerá.

### Experiência Automática

O usuário deve apertar o botão referente a jogar, e será mostrado a ele os caminhos que ele deve seguir para gastar menos.
