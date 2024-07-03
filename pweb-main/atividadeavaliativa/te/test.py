f1=1
while (f1==1):
    
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
            nome=[0,0]
            nomec=[0,0]
            idadec=[0,0]
            idadea=[0,0]
            cpf=[0,0]
            print("Digite o nome:")
            nome [0]=str(input())
            print("Dgite a idade:")
            idadea [0]=int(input())
            print("Informe o cpf:")
            cpf[0]=int(input())
            print("Digite o nome:")
            nome [1]=str(input())
            print("Dgite a idade:")
            idadea [1]=int(input())
            print("Informe o cpf:")
            cpf[1]=int(input())
        if(op==1.2):
            print("Nome da criança:")
            nomec[0]=str(input())
            print("Idade da criança:")
            idadec[0]=int(input())
            print("Nome da criança:")
            nomec[1]=str(input())
            print("Idade da criança:")
            idadec[1]=int(input())
        if(op==1.3):
            f1
    if(opc==2):
        print("O nome do monitor(a):", nome)
        print("A idade do monitor(a):", idadea)
        print("O CPF do monitor(a)", cpf) 
        print("O nome da criança:", nomec)
        print("A idade da criança:", idadec)
    if(opc==3):
        f1=0
print("Agradecemos a preferencia!")           