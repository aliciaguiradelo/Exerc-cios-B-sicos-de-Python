n = input("Digite seu nome:")
s = input("Digte seu sexo:")
estado = input("Digite seu estado civil:")
if(((s.upper()=="F") or (s.upper()=="FEMININO") or (s.upper()=="FEM")) and (estado.upper()=="CASADA")):
    a =print(n.upper(),"você está",estado.upper(), "há quantos anos?")
else:
    print("FIM")