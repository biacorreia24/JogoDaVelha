def jogodavelha():
    tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9] #lista com o número de cada posição da tabela
    acabou = False #continuação do jogo
    quadradomagico = [4, 9, 2, 3, 5, 7, 8, 1, 6] #lista com o número das posições do quadrado mágico para a verificação do ganhador



    def mostrartabela():
        print()
        print('', tabela[0], "|", tabela[1], "|", tabela[2])
        print("---|---|---")
        print('', tabela[3], "|", tabela[4], "|", tabela[5])
        print("---|---|---")
        print('', tabela[6], "|", tabela[7], "|", tabela[8])
        print()
# código para exibir a tabela com as cordenadas



    def verificarjogada():
        jogada = input("Informe sua jogada : ")

        fornumero = True
        for caractere in jogada:
            if caractere < '0' or caractere > '9':
                fornumero = False
        if fornumero:
            jogada = int(jogada)
            if jogada in range(1, 10):

                print(f"Você jogou: {jogada}")
                return jogada
            else:
                print("Jogada Inválida, Tente Novamente !!!")
                return verificarjogada()
        else:
            print("Jogada Inválida, Tente Novamente !!!")
            return verificarjogada()
# verificar se as entradas são válidas





    def repetiu(jogador):
        espacocolocado = verificarjogada() - 1
        if tabela[espacocolocado] == "X" or tabela[espacocolocado] == "O":
            print("Ops !!! Parece que esse lugar já está preenchido, Tente Novamente !")
            repetiu(jogador)
        else:
            tabela[espacocolocado] = jogador
# verificar se a entrada já não foi jogada antes




    def vencedor(jogador):
        jogadas = 0

        for a in range(9):
            for b in range(9):
                for c in range(9):
                    if a != b and b != c and c != a :
                        if tabela[a] == jogador and tabela[b] == jogador and tabela[c] == jogador:
                            if quadradomagico[a] + quadradomagico[b] + quadradomagico[c] == 15:
                                print("Parabéns jogador", jogador, "você é o VENCEDOR !!!")
                                return True

        for d in range(9):
            if tabela[d] == "X" or tabela[d] == "O":
                jogadas += 1
            if jogadas == 9:
                print("EMPATE")
                return True
# verifica se akguém ganhou ou se deu empate, exibindo o resultado




    acabou = False
    while not acabou:
        mostrartabela()
        print("Jogador 1, escolha um espaço.")
        repetiu("X")
        acabou = vencedor("X")

        if not acabou:
            mostrartabela()
            print("Jogador 2, escolha um espaço.")
            repetiu("O")
            acabou = vencedor("O")
    mostrartabela()
# troca os turnos e verifica se o jogo continua ou acaba

jogodavelha()