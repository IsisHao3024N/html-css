f1=1
while(f1==1):
    print("Menu")
    print("1 - Cadastro")
    print("2 - Consulta")
    print("3 - Sair")
    print("Digite a opção desejada:")
    opc=int(input())
    if(opc==1):
        print("1.1 - monitores")
        print("1.2 - Criança")
        print("1.3 - Retornar")
        op=float(input())
        if(op==1.1):
            print("Digite o seu nome:")
            nome=str(input())
            print("Dgite sua idade:")
            idade=int(input())
        if(op==1.2):
            print("Digite o nome da criança:")
            nomec=str(input())
            print("Digite a idade da criança:")
            idadec=int(input())
        if(op==1.3):
            f1
    if(opc==2):
        print("Nome da criança:", nomec)
        print("A idade da criança:", idadec)
    if(opc==3):
        f1=0
print("Agradecemos a preferencia!")