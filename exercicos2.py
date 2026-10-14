import os
import sys

#-----QUESTAO 01-----#
numero = int(input("DIGITE UM VALOR: "))
os.system("cls")
if numero % 2 == 0:
    print(f"O NUMERO {numero} É PAR")
else:
    print(f"O NUMERO {numero} É IMPAR")
opcao = str(input("VOCE QUER CONTINUAR: "))
if opcao == "S":
    os.system("cls")
elif opcao == "N":
    os.system("cls")
    print("PROGRAMA ENCERRADO COM SUCESSO...")
    sys.exit()

#-----QUESTAO 02-----#
idade = int(input("DIGITE SUA IDADE: "))
os.system("cls")
if idade >= 0 and idade <= 12:
    print(f"COM {idade} anos voce é uma Criança")
elif idade >= 13 and idade < 18:
    print(f"COM {idade} anos voce é uma Adolescente")
else:
    print(f"COM {idade} anos voce é uma Adulto")
opcao = str(input("VOCE QUER CONTINUAR: "))
if opcao == "S":
    print("Continuando..")
    os.system("cls")
elif opcao == "N":
    os.system("cls")
    print("PROGRAMA ENCERRADO COM SUCESSO...")
    sys.exit()

#-----QUESTAO 03-----#
loginUser = "to.brasil"
senhaUser = "401020@"
user = input("DIGITE SEU USUARIO: ")
senha = input("DIGITE SUA SENHA: ")
os.system("cls")
if user == loginUser and senha == senhaUser:
    print(f"BEM VINDO AO SISTEMA {user}")
else:
    print("USUARIO OU SENHA ESTAO ERRADOS. VERIFIQUE E TENTE NOVAMENTE")
opcao = str(input("VOCE QUER CONTINUAR: "))
if opcao == "S":
    print("Continuando..")
    os.system("cls")
elif opcao == "N":
    os.system("cls")
    print("PROGRAMA ENCERRADO COM SUCESSO...")
    sys.exit()
    
#-----QUESTAO 04-----#
pontoX = int(input("DIGITA AS COORDENADAS  X: "))
pontoY = int(input("DIGITA AS COORDENADAS  Y: "))
os.system("cls")
if (pontoX > 0 and pontoY > 0):
    print(f"OS VALORES {pontoX} e {pontoY} ESTAO NO PRIMEIRO QUADRANTE")
elif (pontoX < 0 and pontoY > 0):
    print(f"OS VALORES {pontoX} e {pontoY} ESTAO NO SEGUNDO QUADRANTE")
elif (pontoX < 0 and pontoY < 0):
    print(f"OS VALORES {pontoX} e {pontoY} ESTAO NO TERCEIRO QUADRANTE")
elif (pontoX > 0 and pontoY < 0):
    print(f"OS VALORES {pontoX} e {pontoY} ESTAO NO QUARTO QUADRANTE")
else:
    print(f"OS VALORES {pontoX} e {pontoY} ESTAO LOCALIZADOS NO EIXO OU ORIGEM")
opcao = int(input("DIGITE 0 PARA ENCERRAR O PROGRAMA: "))
os.system("cls")
if opcao == 0:
     print("PROGRAMA ENCERRADO COM SUCESSO...")
