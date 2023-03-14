from utils import ApiGithub as ag
while True:
    login = input("Digite o login que deseja consultar:  ")
    dados=ag.consultaGithub(login)
    if (dados != ''):
        print(f"LOGIN: {dados['login']}")
        print(f"SEGUINDO: {dados['following']}")
        print(f"SEGUIDORES: {dados['followers']}")
        print(f"REPOSITÓRIOS PÚBLICOS: {dados['public_repos']}")
        print(f"REPOSITÓRIOS PRIVADOS: {dados['hireable']}")
    else:
        print("LOGIN não encontrado.")
    retorno = input ("Deseja realizar uma nova consulta? S/N")
    if retorno == 'n':
        break
print("Obrigada!")