#!/usr/bin/env python

import sys
from sudoku import Sudoku


def string_pra_array(entrada, tamanho):
    lista = []
    for i in range(0, len(entrada), tamanho):
        lista.append(entrada[i:i+tamanho])

    return lista


def busca_largura(entrada, sudoku):
    if "." not in entrada and sudoku.e_possivel(string_pra_array(entrada, 9)):
        return entrada

    resposta = ""
    for i in range(81):
        if entrada[i] == ".":
            for j in range(1, 10):
                aux = entrada[:i] + str(j) + entrada[i + 1:]
                if sudoku.e_possivel(string_pra_array(aux, 9)):
                    resposta = busca_largura(aux, sudoku)
                    if resposta:
                        return resposta
            break
    return resposta


def le_entrada(entrada):
    # Le os dados de entrada
    with open(entrada, 'r') as f:
        arquivo_lido = f.readlines()

    # Remove o \n e adiciona cada linha como uma entrada
    entradas = [line.strip('\n') for line in arquivo_lido]

    entradas_formatadas = []
    for entrada in entradas:
        entradas_formatadas.append(formata_entradas(entrada))

    return entradas_formatadas


def string_to_list(string):
    lista = []
    lista[:0] = string
    return lista


def formata_entradas(entradas):
    entrada_formada = []
    for i in range(0, 81, 9):
        entrada_formada.append(string_to_list(entradas[i: i+9]))

    return entrada_formada


def imprime(sudoku):
    print("Número de jogos: " + str(len(sudoku)))

    for jogos in sudoku:
        print("---------------------------------------------")
        for jogo in jogos:
            print(jogo)


def output(sudoku):
    aux = ""
    for i in range(9):
        for j in range(9):
            aux += (sudoku[i][j])

    print(aux)


def main():
    entradas = le_entrada(sys.argv[1])
    s_problema = Sudoku(entradas)

    respostas = []
    for jogos in entradas:
        entrata_string = ""
        for linha in jogos:
            for e in linha:
                entrata_string += str(e)

        respostas.append(busca_largura(entrata_string, s_problema))

    saida = ""
    for resposta in respostas:
        saida += resposta + "\n"

    print(saida)


if __name__ == '__main__':
    main()
