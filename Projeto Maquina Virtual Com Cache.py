# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:48:56 2020

@author: DARLAN B AJLUNE

9 + 9 + 11 + 3 = 32 BITS
    
TIPO R
    
    COMMANDE -> [RT] [RS] [RD] [OP]
    
    COMMANDOU -> [RT] [RS] [RD] [OP]
    
    COMMANDSUM -> [RT] [RS] [RD] [OP]
    
    COMMANDSUB -> [RT] [RS] [RD] [OP]
    
TIPO I
    
    COMMANDSUMC -> [CONST] [RS] [RD] [OP]

    COMMANDSUBC -> [CONST] [RS] [RD] [OP]

REGISTRADORES
    A, B, C, D, E, F, G, H, I, J, PC
    
"""
from random import randint
import numpy as np

# DICIONÁRIO COM TODOS OS OPCODES DISPONÍVEIS
OPCODE = {'commandE':'000', 'commandOU':'001', 'commandSUM':'010', 'commandSUB':'011', 'commandSUMC':'100', 'commandSUBC':'101'}
# DICIONÁRIO QUE IRÁ SALVAR TODOS OS REGISTRADORES DISPONÍVEIS 
REGISTER = {}
MEMORYCACHE = np.zeros(shape=(2, 4), dtype=dict)
    
def mostrarRegistradoresInstrucao(instrucaoEmPartes):
    '''
    ESTA FUNÇÃO É USADA PARA MOSTRAR OS REGISTRADORES DAQUELA INSTRUÇÃO E SEUS RESPECTIVOS VALORES
    -------
    Parameters
    ----------
    instrucaoEmPartes : LIST DE STR
        É UMA LISTA QUE SALVA SEPARADAMENTE UMA INTRUÇÃO, OU SEJA:
            POSIÇÃO 0: RT (REGISTRADOR ORIGEM 2) OU CONST (CONSTANTE), VAI DEPENDER DO TIPO DA INSTRUÇÃO, SE É R OU I 
            POSIÇÃO 1: RS (REGISTRADOR ORIGEM 1)
            POSIÇÃO 2: RD (REGISTRADOR DESTINO)
            POSIÇÃO 3: OPCODE (QUAL OPERAÇÃO SERÁ EXECUTADA)
    Returns
    -------
    None.
    
    '''
    
    if int(instrucaoEmPartes[3],2) < 4:
        print(instrucaoEmPartes[2], '=', REGISTER[ int(instrucaoEmPartes[2],2) ])
        print(instrucaoEmPartes[1], '=', REGISTER[ int(instrucaoEmPartes[1],2) ])
        print(instrucaoEmPartes[0], '=', REGISTER[ int(instrucaoEmPartes[0],2) ])
    else:
        print(instrucaoEmPartes[2], '=' , REGISTER[ int(instrucaoEmPartes[2],2) ])
        print(instrucaoEmPartes[1], '=', REGISTER[ int(instrucaoEmPartes[1],2) ])
        print('CONST =', int(instrucaoEmPartes[0],2))

def executandoInstrucao(instrucaoEmPartes):
    '''
    ESTA FUNÇÃO IRÁ EXECUTAR A INSTRUÇÃO DESEJA, PODENDO SER & | + -
    AO FINAL DELA O REGISTRADOR DESTINO TERÁ SEU VALOR ALTERADO
    ----------
    Parameters
    ----------
    instrucaoEmPartes : LIST DE STR
        É UMA LISTA QUE SALVA SEPARADAMENTE UMA INTRUÇÃO, OU SEJA:
            POSIÇÃO 0: RT (REGISTRADOR ORIGEM 2) OU CONST (CONSTANTE), VAI DEPENDER DO TIPO DA INSTRUÇÃO, SE É R OU I 
            POSIÇÃO 1: RS (REGISTRADOR ORIGEM 1)
            POSIÇÃO 2: RD (REGISTRADOR DESTINO)
            POSIÇÃO 3: OPCODE (QUAL OPERAÇÃO SERÁ EXECUTADA)
    Returns
    -------
    None.
    
    '''
    
    print('INSTRUÇÃO A SER EXECUTADA:', *instrucaoEmPartes)
    print('\nREGISTRADORES ANTES')
    mostrarRegistradoresInstrucao(instrucaoEmPartes)
    
    if int(instrucaoEmPartes[3],2) == 0:
        REGISTER[ int(instrucaoEmPartes[2],2) ] = REGISTER[ int(instrucaoEmPartes[1],2) ] & REGISTER[ int(instrucaoEmPartes[0],2) ] 
    elif int(instrucaoEmPartes[3],2) == 1:
        REGISTER[ instrucaoEmPartes[2] ] = REGISTER[ instrucaoEmPartes[1] ] | REGISTER[ instrucaoEmPartes[0] ]
    elif int(instrucaoEmPartes[3],2) == 2:
        REGISTER[ int(instrucaoEmPartes[2],2) ] = REGISTER[ int(instrucaoEmPartes[1],2) ] + REGISTER[ int(instrucaoEmPartes[0],2) ]
    elif int(instrucaoEmPartes[3],2) == 3:
        REGISTER[ int(instrucaoEmPartes[2],2) ] = REGISTER[ int(instrucaoEmPartes[1],2) ] - REGISTER[ int(instrucaoEmPartes[0],2) ]
    elif int(instrucaoEmPartes[3],2) == 4:
        REGISTER[ int(instrucaoEmPartes[2],2) ] = REGISTER[ int(instrucaoEmPartes[1],2) ] + int(instrucaoEmPartes[0],2)
    elif int(instrucaoEmPartes[3],2) == 5:
        REGISTER[ int(instrucaoEmPartes[2],2) ] = REGISTER[ int(instrucaoEmPartes[1],2) ] - int(instrucaoEmPartes[0],2)
    
    print('\nREGISTRADORES DEPOIS')
    mostrarRegistradoresInstrucao(instrucaoEmPartes)
    print('*******************************************************')   
    
def mostraRegistradores():
    '''
    ESTÁ FUNÇÃO IRÁ MOSTRAR TODOS OS REGISTRADORES E SEUS RESPECTIVOS VALORES
    -------
    Returns
    -------
    None.

    '''
    
    for i in range(10):
        print(chr(ord('A')+i),'=', REGISTER[i])

def fetchCache(INSTRUCOES, PC):
    '''
    Parameters
    ----------
    INSTRUCOES : LIST DE STR
        É UMA LISTA QUE SALVA TODAS AS INSTRUÇÕES, ONDE CADA POSIÇÃO SALVA UMA DELAS, POR EXEMPLO:
            POSIÇÃO 0: "A B C COMMANDE"
            POSIÇÃO 1: "I J B COMMANDSUB"
    PC : INT
        REPRESENTA QUAL INSTRUÇÃO SERÁ EXECUTADA, POR EXEMPLO.
             PC = 0 -> 1º INSTRUÇÃO
             PC = 1 -> 2º INSTRUÇÃO
             PC = 2 -> 3º INSTRUÇÃO
   
    Returns
    -------
    RETORNA UM STR
        RETORNA A INSTRUÇÃO QUE SERÁ EXECUTADA.

    '''

    binarioPC = np.binary_repr(PC, 32)
    c = int(binarioPC[-2:], 2)
    l = int(binarioPC[-3], 2)
    tag = int(binarioPC[:-3], 2)
    
    if not(MEMORYCACHE[l, c]['VALIDO'] and MEMORYCACHE[l, c]['TAG'] == tag):
        print('CACHE MISS')
        pos = 0
        for i in range(2):
            for j in range(4):
                if len(INSTRUCOES) != PC+pos:
                    MEMORYCACHE[i, j]['VALIDO'] = True
                    MEMORYCACHE[i, j]['TAG'] = tag
                    MEMORYCACHE[i, j]['DATA'] = INSTRUCOES[PC+pos]
                    pos += 1
    else:
        print('CACHE HIT')
    
    return MEMORYCACHE[l, c]['DATA']


def inicializacaoRegistradores():
    '''
    FUNÇÃO QUE INICIALIZA OS REGISTRADORES COM UM VALOR ALEATÓRIO ENTRE 0 E 511 
    -------
    Returns
    -------
    None.

    '''
    print('INICIALIZANDO OS REGISTRADORES')
    for i in range(10):
        REGISTER[i] = randint(0, 2**9-1)
    
    mostraRegistradores()

    print('*******************************************************')

def inicializacaoCache():
    for i in range(2):
        for j in range(4):
            MEMORYCACHE[i,j] = { 'VALIDO': False, 'TAG': 0,'DATA': 0 }

    

def decodificacaoInstrucao(instrucaoVouExecutar):
    '''
    Parameters
    ----------
    instrucaoVouExecutar : STR
        REPRESENTA A INSTRUÇÃO QUE SERÁ DECODIFICADA EM PARTES E DEPOIS SERÁ FEITO A VERIFICAÇÃO SE ELA É VÁLIDA OU NÃO.

    Returns
    -------
    instrucaoEmPartes : LISTA DE STR
        RETORNA A INSTRUÇÃO DECODIFICADA, OU SEJA, SEPARANDO O OPCODE, OS REGISTRADORES E A CONSTANTE, CASO EXISTIR.

    '''
    global flag
    flag = True

    instrucaoEmPartes = instrucaoVouExecutar.split()
    instrucaoEmPartes[1] = np.binary_repr(ord(instrucaoEmPartes[1])-65, 9)
    instrucaoEmPartes[2] = np.binary_repr(ord(instrucaoEmPartes[2])-65, 9)
    instrucaoEmPartes[3] = OPCODE[instrucaoEmPartes[3]]
    
    if 4 <= int(instrucaoEmPartes[3], 2) <= 5:
        try:
            instrucaoEmPartes[0] = np.binary_repr(int(instrucaoEmPartes[0]), 11)    
        except ValueError:
            print('CONSTANTE INVÁLIDA', instrucaoEmPartes[0])
            flag = False
            return []  
    else:
        try:
            instrucaoEmPartes[0] = np.binary_repr(ord(instrucaoEmPartes[0])-65, 11)
        except TypeError:
            print('REGISTRADOR INVÁLIDA', instrucaoEmPartes[0])
            flag = False
            return []

    if len(instrucaoEmPartes) != 4:
        print('INSTRUÇÃO INVÁLIDO', *instrucaoEmPartes)
        flag = False
        return []
    else:
        if not(0 <= int(instrucaoEmPartes[3],2) <= 5):
            print('OPCODE INVÁLIDO', instrucaoEmPartes[3])
            flag = False
            return []
        else:
            for i in range(3):
                if not(4 <= int(instrucaoEmPartes[3], 2) <= 5 and i == 0) and not(0 <= int(instrucaoEmPartes[i], 2) <= 9):
                    print('REGISTRADOR INVÁLIDO', instrucaoEmPartes[i])
                    flag = False
                    return []

    flag = True
    return instrucaoEmPartes

def main():
    
    '''
    PARA EXECUTAR O CÓDIGO É NECESSÁRIO CRIAR UM ARQUIVO instruções.txt CONTENDO AS INSTRUÇÕES DESEJADAS (SEPARADAS LINHA POR LINHA).
    POR EXEMPLO:
    C B A commandE
    -45 E D commandSUBC
    A B C commandE
    I J B commandSUB        
    -45 D G commandSUMC
    '''
    
    inicializacaoRegistradores()
    inicializacaoCache()
    INSTRUCOES = []
    arquivo = open('instruções.txt', 'r')
    for linha in arquivo:
        INSTRUCOES.append(str(linha))
    
    #INSTRUCOES = ["C B A commandE", "F E D commandSUM"]
    PC = 0
    qtd_instrucao = len(INSTRUCOES)
    while(qtd_instrucao):
        
        instrucaoVouExecutar = fetchCache(INSTRUCOES, PC)
        instrucaoEmPartes = decodificacaoInstrucao(instrucaoVouExecutar)
        if not(flag):
            return
        executandoInstrucao(instrucaoEmPartes)
        
        qtd_instrucao = qtd_instrucao - 1
        PC = PC + 1
        
    print('VALORES FINAIS DOS REGISTRADORES')
    mostraRegistradores()

if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main