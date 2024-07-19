from Interface import *
from dados import *
from verificação import *

def main():
    cabeçario()
    while True:
        try:
            opcao = int(input("""O'que você deseja?
            Insira 1 para inciar um novo jogo;
            Insira 2 para verificar record gerais;
            Insira 3 para verificar record de um determinado jogador;
            Insira 4 para encerrar o programa.
                        """))
            if opcao == 1:
                pedir_nick()
                dificuldade()
                jogo_da_forca()
            elif opcao == 2:
                mostrar_records()
            elif opcao == 3:
                buscar_dados_jogador()
            elif opcao == 4:
                print('Obrigado por jogar!')
                #salvar_record(lista_records)
                break
        except Exception as erro:
            print(f'Infelizmente tivemos um problema! Tente novamente, digitando corretamente na próxima vez!')
            

# Executar o programa
if __name__ == "__main__":
    main()
