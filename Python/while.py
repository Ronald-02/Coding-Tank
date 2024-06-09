numero_sorteado = 15

numero_escolhido = int (input ('Informe um número entre 1 e 100: '))

while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente novamente...')
    
    numero_escolhido = int (input ('Informe um número entre 1 e 100: '))

print('Parabéns! Você acertou!')