def main():
    cabeçario()
    pedir_nick()
    #placar()
    while True:
        opcao = int(input("""O'que você deseja?: """+str(nick)+""""
          Insira 1 para inciar um novo jogo;
          Insira 2 para verificar record gerais;
          Insira 3 para verificar record de um determinado jogador;
          Insira 4 para encerrar o programa.
                          """))
        if opcao == 1:
            dificuldade()
            placar()
        elif opcao == 2:
            print('a')
        elif opcao == 3:
            print('a')
        elif opcao == 4:
            print('Obrigado por jogar!')
            #salvar_record(lista_records)
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == "__main__":
    main()
