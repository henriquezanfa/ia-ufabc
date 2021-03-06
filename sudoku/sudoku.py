from utils import string_pra_array


class Sudoku:

    def __init__(self, initial_state):
        self.initial_state = initial_state

    def expand_nodes(self, current_state):
        # print(current_state)
        expanded_nodes = []
        expanded_nodes = self.actions(current_state)
        return expanded_nodes

    def check_ocurrencies(self, state):
        for x in range(1, 10):
            if state.count(str(x)) > 1:  # str(x) porque os estados são Strings
                return False

        return True

    def e_possivel(self, current_state):
        """
        Não pode haver o mesmo número duas vezes em uma coluna
        Não pode haver o mesmo número duas vezes em uma linha - OK
        Não pode haver o mesmo número duas vezes em um mesmo quadrante
        """

        # Valida se tem repetição numa linha
        for i in range(9):
            aux = []
            for j in range(9):
                aux.append(current_state[i][j])

            if not self.check_ocurrencies(aux):
                return False

        # Valida se tem repetição numa coluna
        for i in range(9):
            aux = []
            for j in range(9):
                aux.append(current_state[j][i])

            if not self.check_ocurrencies(aux):
                return False

        # Valida se tem repetição num quadrante
        aux = [""] * 9
        for i in range(9):
            for j in range(9):
                if i < 3 and j < 3:
                    aux[0] += (current_state[i][j])
                elif i < 3 and j < 6:
                    aux[1] += (current_state[i][j])
                elif i < 3 and j < 9:
                    aux[2] += (current_state[i][j])
                elif i < 6 and j < 3:
                    aux[3] += (current_state[i][j])
                elif i < 6 and j < 6:
                    aux[4] += (current_state[i][j])
                elif i < 6 and j < 9:
                    aux[5] += (current_state[i][j])
                elif i < 9 and j < 3:
                    aux[6] += (current_state[i][j])
                elif i < 9 and j < 6:
                    aux[7] += (current_state[i][j])
                else:
                    aux[8] += (current_state[i][j])

        for i in range(9):
            if not self.check_ocurrencies(aux[i]):
                return False

        return True

    def atingiu_obj(self, estado):
        return estado and "." not in estado and self.e_possivel(string_pra_array(estado, 9))

    def actions(self, current_state):
        """
        Dado o estado atual, retorna as possíveis ações que não
        tornam o problema impossível a partir desse estado e
        retorna a lista dos estados que cada uma dessas ações gera
        """
        novosEstados = []
        # print("ações-----------------")
        estado = current_state
        # current_state.remove(estado)
        for i in range(81):
            if estado[i] == ".":
                for j in range(1, 10):
                    aux = estado[:i] + \
                        str(j) + estado[i + 1:]
                    if self.e_possivel(string_pra_array(aux, 9)):
                        novosEstados.append(aux)
                break

        return novosEstados
