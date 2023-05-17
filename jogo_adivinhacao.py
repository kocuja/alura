import random

def execute():
    print('QUAL O NÚMERO SECRETO?')

    numero_secreto = round(random.randrange(1, 101))
    rodada = 1
    pontos = 1000

    print('ESCOLHA UMA DIFICULDADE: ')
    print('(1) FÁCIL, (2) MÉDIO (3) DIFÍCIL.')

    dificuldade = int(input('Digite um dos números acima: '))

    if dificuldade == 1:
        tentativas = 20
    elif dificuldade == 2:
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print('Tentativa: {} de {}'.format(rodada,tentativas))
        chute = int(input('Tente um número de 1 a 100: '))
        print('Você digitou: {}'.format(chute))

        if (chute < 1 or chute > 100):
            print('Tente novamente com um número de 1 a 100.')
            continue

        numero_correto = chute==numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(numero_correto):
            print('Parabéns! Você acertou!')
            break
        else:
            if(maior):
                print('ERRADO! Valor muito alto!')
            elif(menor):
                print('ERRADO! Valor muito baixo!')

            pontos_perdidos = abs(numero_correto - chute)
            pontos = pontos - pontos_perdidos

    print(f'FIM DO JOGO, você fez {pontos} pontos!')
   
if __name__ == '__main__':
    execute()
