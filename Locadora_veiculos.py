import os
from time import sleep

carros = [
("Chevrolet Tracker",120),
("Chevrolet S10",150),
("Chevrolet onix",90),
("Chevrolet Spin",150),
("Hyundai HB20",85),
("Hyundai Tucson",120),
("Fiat Uno",60),
("Fiat Mobi",70),
("Fiat Estrada",100),
]
alugados = []

def mostrar_lista_de_carros(lista_carros):
    for i,car in enumerate(lista_carros):
        print(f'[{i}] {car[0]} - R${car[1]} /dia.')

while True:
    os.system('cls')
    print('='*5)
    print('[LOCAR- Aluguel de Veiculos] - Seja bem vindo')
    print('=' * 5)
    print('O que deseja fazer?\n0 - Mostrar Portifólio | 1 - Alugar carro | 2 - Devolver um carro')
    op=int(input(''))
    os.system('cls')
    if op==0:
        mostrar_lista_de_carros(carros)
    elif op==1:
        mostrar_lista_de_carros(carros)
        print('=' * 5)
        cod_carro=int(input('qual codigo do carro escolhido:'))
        dias=int(input('por quantos dias você irá alugar:'))
        os.system('cls')

        print(f'Você escolheu o {carros[cod_carro][0]} , por {dias} dias,')
        print(f'O seu aluguel vai custar R${(carros[cod_carro][1])*dias}')
        sleep(0.5)
        print('Você deseja confirmar o aluguel?')
        conf=int(input('[0] para SIM | 1 para NÂO:'))
        if conf == 0:
            print(f'Parabéns!!\nVocê alugou o carro {carros[cod_carro][0]} por {dias} dias')
            alugados.append(carros.pop(cod_carro))
    elif op==2:
        if len(alugados) == 0:
            print('Não há carros para devolver.')
        else:
            print('Segue a lista de carros alugados:')
            sleep(0.7)
            mostrar_lista_de_carros(alugados)
            print('')
            cod_devo = int(input('Escolha o codigo do carro que deseja devolver:'))
            if conf ==0:
                print(f'Obrigado por devolver {alugados[cod_devo][0]}')
                carros.append(alugados.pop(cod_devo))
    print('='*5)
    print('[0] para continuar | [1] para sair')
    if int(input()) ==1:
        break