#!/usr/bin/python
# -*- coding: UTF-8 -*-

# soma = 0
# sub = 0
# mult = 1
# div = 1


def soma():
    total = 0
    num = 0
    while num != '=':
        num = input('Número: ')
        if num != '=':
            total += float(num)
        continue

    print(total)


def subtracao():
    print(1-1)
    pass


def divisao():
    print(1/1)
    pass


def multiplicacao():
    print(1*1)
    pass


# Função de decisão da operação
def decisao(opcao):
    if opcao == '+':
        soma()
    elif opcao == '-':
        subtracao()
    elif opcao == '/':
        divisao()
    elif opcao == '*':
        multiplicacao()
    pass


# Função inicial por onde começa o srcipt
def main():
    operador = str(input('Digite o operador: '))
    # Verificação do operador
    if (operador != '+' and operador != '-' and operador != '*' and operador != '/'):
        print('Operador inválido.')
        main()
    else:
        decisao(operador)


# Solicitação do número e verificação do gatilho de parada

# while True:
#     num = input('Número: ')

# Soma
    # if operador == '+':
    #     if num == '=':
    #         print(soma)
    #         break
    #     else:
    #         num = float(num)
    #         soma += num
    #         continue
# Subtração

    # elif operador == '-':
    #     if num == '=':
    #         print(sub)
    #         break
    #     else:
    #         num = float(num)
    #         sub = num - sub
    #         if num < sub:
    #             sub = abs(sub)
    #         else:
    #
    #
    #         continue

# Multiplicação

    # elif operador == '*':
    #     if num == '=':
    #         print(mult)
    #         break
    #     else:
    #         num = float(num)
    #         mult *= num
    #         continue
# Divisão

    # elif operador == '/':
    #     if num == '=':
    #         print(div)
    #         break
    #     else:
    #         num = float(num)
    #         div = num/div
    #
    #         continue
    # break


main()
