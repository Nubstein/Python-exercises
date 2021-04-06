# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random  #para pega aleatóriamente as palavras do arquivo

# Board (tabuleiro)   #abre uma lista [ de caracteres desenhando o homem,
                      #cada um item da lista contém a pessoa com uma chance a menos e um órgão comprometido
board = ['''           

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word): #quando o objeto for instanciado, teremos que passar uma palavra como parametro
        self.word = word
        self.missed_letters = []  #listas vazias para letras erradas
        self.guessed_letters = []   #listas vazia para letras certas

    # Método para adivinhar a letra, recebe parâmetro uma letra
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:#se a letra está dentro da palavra e letra nao dentro de letras certas
            self.guessed_letters.append(letter) #adicionar esta letra dentro da lista de letras corretas
        elif letter not in self.word and letter not in self.missed_letters: #se a letra nao estiver na palavra, e também nao estiver na lista de palavras erradas
            self.missed_letters.append(letter) #adicionar essa letra na lista de palavras erradas
        else:
            return False
        return True  #E importante dar um retorno para seu método

    # Método para verificar se o jogo terminou
    def hangman_over(self):                      #6 tentativas de 2 braços, 2 pernas, cabeça e corpo
        return self.hangman_won() or (len(self.missed_letters) == 6)

    # Método para verificar se o jogador venceu
    def hangman_won(self):   # "_" forma que usamos para oculta as letras da palavra, e saber se completei ou nao a palavra
        if '_' not in self.hide_word(): #se ainda houver algum __ é pq o jogo ainda não acabou
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ''   #string vazia que vai receber alguma coisa
        for letter in self.word:  #para cada letra dentro da palavra
            if letter not in self.guessed_letters:  #se a letra nao estiver em palavras certas
                rtn += '_'                          #preencho com "_"
            else:
                rtn += letter            #se estiver preencho com a letra
        return rtn

    # Método para checar o status do game e imprimir o board na tela
    #board é uma lista, entao posso acessar as posições, através de indices []
        def print_game_status(self):
            print(board[len(self.missed_letters)]) # aqui o cumprimento das palavras erradas indica o indice [] do board, que é uma lista
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras erradas: ', )
        for letter in self.missed_letters: #para cada letra na lista de letras erradas
            print(letter, )                #imprimir a letra
        print()
        print('Letras corretas: ', )   #imprimir letras corretas
        for letter in self.guessed_letters: #para cada letra na lista de letras corretas
            print(letter, )                 #imprimi a letra
        print()

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_word(): #função para definir palara aleatória
    with open("palavras.txt", "rt") as f: #abrir arquivo com as palavras
        bank = f.readlines()  #lê uma única linha
    return bank[random.randint(0, len(bank))].strip() #busca uma linha dentro do txt, a cada execução será outra palavra


# Método Main - Execução do Programa
def main():
    # Objeto sendo instanciado, parametro será gerado aleatoriamente pela rand_word
    game = Hangman(rand_word())

    #Importante verificar a identação, sempre dentro do main
    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over(): #enquanto jogo nao acabou
        game.print_game_status()
        user_input = input('\nDigite uma letra: ') #enquanto nao acabar, continua pedindo o usuário para inserir letra
        game.guess(user_input) #Chamar o método guess, para adivinhar a palavra inserindo letra

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word) #para saber qual é a palavra correta

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
