# -*- coding: utf-8 -*-
arquivo = open('EBNF02.txt','r')
separandoLinhas = []
resultado = []

for linha in arquivo:
    separandoLinhas.append(linha.replace('\n',''))

del(separandoLinhas[0])

def inicio(valor):
    for linha in range(len(valor)):
        resultado.append(validacao(separandoLinhas[linha]))
        print(resultado[linha])

def abreParen(valor, posicao):
    if valor[posicao] == '(':
        return True
    else:
        return False

def fechaParen(valor, posicao):
    if valor[posicao] == ')':
        return True
    else:
        return False

def proposicao(valor, posicao=0):
    prop = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',\
    'r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    if [x for x in prop if x == valor[posicao]]:
        return True
    else:
        return False  

def operadorUnario(valor, posicao):
    if valor[posicao] == '!':
        return True
    else:
        return False

def operadorBinario(valor,posicao):
    if valor[posicao] == 'V' or valor[posicao] == '^' or valor[posicao] == '>':
        return True
    if posicao < len(valor) - 1:
        if valor[posicao] == '<' and valor[posicao + 1] == '>':
            return True
        else:
            return False
    elif valor[posicao] == '<' and posicao == len(valor) - 1:
        return True
    else:
        return False

def constante (valor,posicao):
    if valor[posicao] == 'T':
        return True
    elif valor[posicao] == 'F':
        return True
    else:
        return False

def validacao(valor,posicao=0):
    const = 0
    prop = 0
    abre = 0
    fecha = 0
    opUn = 0
    opBin = 0
    opBinE = 0
    while posicao < len(valor) - 1:
        if valor[posicao] == '(' and posicao < len(valor) - 1:
            if abreParen(valor,posicao) and posicao < len(valor) - 1:
                abre += 1
                posicao += 1
        if valor[posicao] != '(' and posicao < len(valor) - 1:
            if operadorUnario(valor,posicao) and posicao < len(valor) - 1:
                opUn += 1
                posicao += 1
            if constante(valor,posicao) and posicao < len(valor) - 1:             
                const += 1
                posicao += 1
            if proposicao(valor,posicao) and posicao < len(valor) - 1:
                prop += 1
                posicao += 1
            if operadorBinario(valor,posicao) and posicao < len(valor) - 1:
                opBin += 1
                posicao += 1
            if valor[posicao] == '<' and posicao < len(valor) - 1:
                opBinE += 1
                posicao+=1
        if valor[posicao] == ')':
            if fechaParen(valor,posicao) and posicao < len(valor) - 1:
                fecha += 1
                posicao += 1

        if valor[posicao] == '(' and posicao == len(valor) - 1:
            if abreParen(valor,posicao) and posicao == len(valor) - 1:
                abre += 1
                #posicao += 1
        if valor[posicao] != '(' and posicao == len(valor) - 1:
            if operadorUnario(valor,posicao) and posicao == len(valor) - 1:
                opUn += 1
                #posicao += 1
            if constante(valor,posicao) and posicao == len(valor) - 1:             
                const += 1
                #posicao += 1
            if proposicao(valor,posicao) and posicao == len(valor) - 1:
                prop += 1
                #posicao += 1
            if operadorBinario(valor,posicao) and posicao == len(valor) - 1:
                opBin += 1
                #posicao += 1
            if valor[posicao] == '<' and posicao == len(valor) - 1:
                opBinE += 1
                #posicao+=1
        if valor[posicao] == ')':
            if fechaParen(valor,posicao) and posicao == len(valor) - 1:
                fecha += 1
                posicao += 1
    if abre == fecha and opUn > 0 and const > 0 and prop == 0 and opBin == 0 and opBinE == 0:
        return 'valido'
    elif abre == fecha and opUn > 0 and const == 0 and prop > 0 and opBin == 0 and opBinE == 0:
        return 'valido'
    elif abre == fecha and opUn == 0 and const == 0 and prop > 0 and opBin > 0 and opBinE == 0:
        return 'valido'
    elif abre == fecha and opUn == 0 and const > 0 and prop == 0 and opBin > 0 and opBinE == 0:
        return 'valido'
    elif abre == fecha and opUn == 0 and const == 0 and prop > 0 and opBin == 0 and opBinE == 0:
        return 'valido'
    elif abre == fecha and opUn == 0 and const > 0 and const < 2 and prop == 0 and opBin == 0 and opBinE == 0:
        return 'valido'
    else:
        return 'invalido'

    #print(const, prop, abre, fecha, opUn, opBin, opBinE)

inicio(separandoLinhas)
