#!/usr/bin/env python

import sys
from sudoku import Sudoku
import time
import utils


def busca_largura(entrada, sudoku):
    estados = sudoku.expand_nodes(entrada)

    for e in estados:
        if sudoku.atingiu_obj(e):
            return e

    return busca_largura(estados, sudoku)


def main():
    entradas = utils.le_entrada(sys.argv[1])
    s_problema = Sudoku(entradas)

    start = time.time()
    respostas = []
    for jogos in entradas:
        entrata_string = ""
        for linha in jogos:
            for e in linha:
                entrata_string += str(e)

        respostas.append(busca_largura([entrata_string], s_problema))

    saida = ""
    for resposta in respostas:
        saida += resposta + "\n"

    # print(saida)

    end = time.time()

    print(end-start)


if __name__ == '__main__':
    main()
