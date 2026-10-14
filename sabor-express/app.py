import os

def limpar():
     os.system("cls")
nomes_restaurantes = ["PIZZA","SUSHI","CARNE"]

def nome_do_programa():
    print ("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")
    
def opcao():
    print("\n 1 Cadastrar Restaurante")
    print("\n 2. Listar Restaurantes")
    print("\n 3. Ativar Restaurante")
    print("\n 4. Sair\n")

def opcao_invalida():
    limpar()
    nome_do_programa()
    print("OPÇÃO INVALIDA\n")
    input("APERTE QUALQUER TECLA PARA VOLTAR AO MENO PRINCIPA: ")
    main()

def finalizar_app():
        limpar()
        nome_do_programa()
        print("ENCERRENDO O APP...\n")

def cadastrar_restaurante():
    limpar()
    nome_do_programa()
    print("BEM VINDO AO CADASTRO DE NOVOS RESTAURANTES\n")
    restaurantes = input("Nome do restaurante: ")
    nomes_restaurantes.append(restaurantes)
    print(f"O RESTAURANTE {restaurantes} FOI CADASTRADO COM SUCESSO")
    escolha = input(" CONTINUAR OU PARAR: ")
    if escolha == "CONTINUAR" or escolha == "continuar" or escolha == "Continuar":
        cadastrar_restaurante()
    elif escolha == "PARAR" or escolha == "parar" or escolha == "Parar":
        limpar()
        nome_do_programa()
        input("APERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL: ")
        main()
    else:
        opcao_invalida()

def listar_restaurantes():
    limpar()
    nome_do_programa()
    print("BEM VINDA A LISTA DE RESTAURANTES\n")
    if nomes_restaurantes == []:
        print("VOCE PRECISA CADASTRAR RESTAURANTES PARA LISTAR ELES!\nVOLTE A OPCAO NUMERO 1 PARA VER A LISTA DE RESTAURANTES CADASTRADOS\n")
        escolha = int(input("DIGITE 0 PARA VOLTAR AO MENU PRINCIPAL OU DIGITE 1 PARA CADASTRAR RESTAURANTES: "))
        if (escolha == 0):
            main()
        elif (escolha == 1):
            cadastrar_restaurante()
        else:   
            opcao_invalida()
    else:
        i = 1
        for nome_restaurante in nomes_restaurantes:
            print(f"{i}.{nome_restaurante}")
            i+=1
        input("\nAPERTE QUALQUER TECLA PARA VOLTAR AO MENU PRINCIPAL: ")
        main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha a opcao desejada:"))
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("BEM VINDO A ATIVACAO DE SEU RESTAURANTE")
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar()
    nome_do_programa()
    opcao()
    escolher_opcao()  

if __name__ == "__main__":  
    main()

