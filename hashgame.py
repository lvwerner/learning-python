def print_tabuleiro(tab):
    for i in range(3):
        print(tab[i])

def check_ganhador(tab, jogador):
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] == jogador:  # linha
            return True
        if tab[0][i] == tab[1][i] == tab[2][i] == jogador:  # coluna
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] == jogador:  # diagonal
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] == jogador:  # diagonal
        return True
    return False

def jogo_da_velha():
    tab = [[' ' for _ in range(3)] for _ in range(3)]
    jogador = 'X'
    while True:
        print_tabuleiro(tab)
        linha = int(input("Digite a linha para " + jogador + ": "))
        coluna = int(input("Digite a coluna para " + jogador + ": "))
        tab[linha][coluna] = jogador
        if check_ganhador(tab, jogador):
            print("Jogador", jogador, "ganhou!")
            break
        jogador = 'O' if jogador == 'X' else 'X'  # troca de jogador

jogo_da_velha()