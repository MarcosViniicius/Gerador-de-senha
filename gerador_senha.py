from random import choice

class GeradorDeSenha:
    def __init__(self):
        pass
    def gerador_senha(self):
        maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        minusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numeros   = ['1','2','3','4','5','6','7','8','9']
        especiais = ['@', '#', '!']

        tamanho = int(input('Escolha o tamanho da sua senha: '))
        escolha = int(input('Qual formato quer seguir na sua senha?\n1. Apenas maiúsculas\n2. Apenas minúsculas\n3. Apenas números\n4.Aleatória(incluindo caracteres especiais)\nESCOLHA: '))


        if escolha == 1:
            escolha = maiusculo
        elif escolha == 2:
            escolha = minusculo
        elif escolha == 3:
            escolha = numeros
        elif escolha == 4:
            escolha = maiusculo + minusculo + numeros + especiais






        senha = ''
        for i in range(tamanho):
            senha += choice(escolha)
        print(senha)

