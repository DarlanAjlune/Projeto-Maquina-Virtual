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

# DICIONÁRIO COM TODOS OS OPCODES DISPONÍVEIS
OPCODE = {'commandE':0, 'commandOU':1, 'commandSUM':2, 'commandSUB':3, 'commandSUMC':4, 'commandSUBC':5 }
# DICIONÁRIO QUE IRÁ SALVAR TODOS OS REGISTRADORES DISPONÍVEIS 
REGISTER = {}
    
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
    
    if OPCODE[instrucaoEmPartes[3]] == 0:
        REGISTER[ instrucaoEmPartes[2] ] = REGISTER[ instrucaoEmPartes[1] ] & REGISTER[ instrucaoEmPartes[0] ] 
    elif OPCODE[instrucaoEmPartes[3]] == 1:
        REGISTER[ instrucaoEmPartes[2] ] = REGISTER[ instrucaoEmPartes[1] ] | REGISTER[ instrucaoEmPartes[0] ]
    elif OPCODE[instrucaoEmPartes[3]] == 2:
        REGISTER[ instrucaoEmPartes[2] ] = REGISTER[ instrucaoEmPartes[1] ] + REGISTER[ instrucaoEmPartes[0] ]
    elif OPCODE[instrucaoEmPartes[3]] == 3:
        REGISTER[ instrucaoEmPartes[2] ] = REGISTER[ instrucaoEmPartes[1] ] - REGISTER[ instrucaoEmPartes[0] ]
    elif OPCODE[instrucaoEmPartes[3]] == 4:
        REGISTER[ instrucaoEmPartes[2] ] = REGISTER[ instrucaoEmPartes[1] ] + int(instrucaoEmPartes[0])
    elif OPCODE[instrucaoEmPartes[3]] == 5:
        REGISTER[ instrucaoEmPartes[2] ] = REGISTER[ instrucaoEmPartes[1] ] - int(instrucaoEmPartes[0])
    
    print('\nREGISTRADORES DEPOIS')
    mostrarRegistradoresInstrucao(instrucaoEmPartes)
    print('*******************************************************')   
    
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
    
    if OPCODE[instrucaoEmPartes[3]] < 4:
        print(instrucaoEmPartes[2], '=', REGISTER[ instrucaoEmPartes[2] ])
        print(instrucaoEmPartes[1], '=', REGISTER[ instrucaoEmPartes[1] ])
        print(instrucaoEmPartes[0], '=', REGISTER[ instrucaoEmPartes[0] ])
    else:
        print(instrucaoEmPartes[2], '=' , REGISTER[ instrucaoEmPartes[2] ])
        print(instrucaoEmPartes[1], '=', REGISTER[ instrucaoEmPartes[1] ])
        print('CONST =', instrucaoEmPartes[0])

def mostraRegistradores():
    '''
    ESTÁ FUNÇÃO IRÁ MOSTRAR TODOS OS REGISTRADORES E SEUS RESPECTIVOS VALORES
    -------
    Returns
    -------
    None.

    '''
    
    for i in range(10):
        print(chr(ord('A')+i),'=', REGISTER[chr(ord('A')+i)])
        
# RETORNA A INSTRUÇÃO A SER EXECUTADA    
def fetch(INSTRUCOES, PC):
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
    return INSTRUCOES[PC]
    
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
        REGISTER[chr(ord('A')+i)] = randint(0, 2**9-1)
    
    mostraRegistradores()
    print('*******************************************************')
    
def ehDigito(x):
    '''
    Parameters
    ----------
    x : STR
        X É O RT OU CONST.

    Returns
    -------
    BOOLEANO
        RETORNA TRUE SE X FOR UM DÍGITO OU FALSE CASO CONTRÁRIO.
    '''
    if x[0] == '-':
        aux = x.split('-')
        if len(aux) != 2:
            return False
        else:
            return (aux[1].isdigit())
    else: 
        return x.isdigit()
    
def validaInstrucao(instrucaoEmPartes):
    '''
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
    BOOLEANO
        RETORNA TRUE SE A INSTRUÇÃO FOR VÁLIDA OU FALSE CASO CONTRÁRIO.

    '''
    if len(instrucaoEmPartes) != 4:
        print('INSTRUÇÃO INVÁLIDO', *instrucaoEmPartes)
        return False
    else:
        if OPCODE.get(instrucaoEmPartes[3]) == None:
            print('OPCODE INVÁLIDO', instrucaoEmPartes[3])
            return False
        
        if 4 <= OPCODE[instrucaoEmPartes[3]] <= 5 and not(ehDigito(instrucaoEmPartes[0])):
            print('CONSTANTE INVÁLIDA', instrucaoEmPartes[0])
            return False
        
        for i in range(3):
            if REGISTER.get(instrucaoEmPartes[i]) == None and not( 4 <= OPCODE[instrucaoEmPartes[3]] <= 5):
                print('REGISTRADOR INVÁLIDO', instrucaoEmPartes[i])
                return False
    
    return True    
        

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
    instrucaoEmPartes = instrucaoVouExecutar.split()
    global flag
    flag = validaInstrucao(instrucaoEmPartes)
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
    INSTRUCOES = []
    arquivo = open('instruções.txt', 'r')
    for linha in arquivo:
        INSTRUCOES.append(str(linha))
    
    #INSTRUCOES = ["C B A commandE", "F E D commandSUM"]
    PC = 0
    qtd_instrucao = len(INSTRUCOES)
    while(qtd_instrucao):
        
        instrucaoVouExecutar = fetch(INSTRUCOES, PC)
        
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