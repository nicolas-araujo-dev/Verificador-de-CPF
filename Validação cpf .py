nome = input('"Olá prazer Qual o seu nome?')

print("Olá", nome, "prazer em te conhecer")

try:  # tratamento de execução
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Você é adolescente")
    elif idade >= 65:
        print("Você é idoso")
    else:
        print("Você é adulto")
except ValueError:
    print("Por favor, insira um número válido para a idade.")

altura = input("Qual a sua altura?")

print(nome, idade, altura, "Essas informações estão corretas? ")

local = input("Onde você mora atualmente?")

print("Esse lugar está correto?", local)


def validacao_cpf(NOVO_CPF):
    # Remove qualquer espaço ou caractere não numérico
    NOVO_CPF = ''.join(filter(str.isdigit, NOVO_CPF))

    if len(NOVO_CPF) != 11:
        print(f"O CPF número: {NOVO_CPF} é inválido, deve ter 11 dígitos.")
        return

    primeiro_dvd = sum(int(NOVO_CPF[i]) * (10 - i) for i in range(9))
    primeiro_digito = 0 if primeiro_dvd < 2 else 11 - (primeiro_dvd % 11)
    primeiro_digito = 0 if primeiro_digito >= 10 else primeiro_digito

    segundo_dvd = sum(int(NOVO_CPF[i]) * (11 - i) for i in range(10))
    segundo_digito = 0 if segundo_dvd < 2 else 11 - (segundo_dvd % 11)
    segundo_digito = 0 if segundo_digito >= 10 else segundo_digito

    if (int(NOVO_CPF[9]) == primeiro_digito) and (int(NOVO_CPF[10]) == segundo_digito):
        print(f"O CPF número: {NOVO_CPF} é válido!")

        # Validação dos estados de origem do CPF
        antepenultimo_digito_cpf = int(NOVO_CPF[8])
        estados = {
            1: "Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins",
            2: "Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima",
            3: "Ceará, Maranhão ou Piauí",
            4: "Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas",
            5: "Bahia e Sergipe",
            6: "Minas Gerais",
            7: "Rio de Janeiro ou Espírito Santo",
            8: "São Paulo",
            9: "Paraná ou Santa Catarina",
            0: "Rio Grande do Sul"
        }
        print(
            f"Seu CPF é originário do estado do {estados.get(antepenultimo_digito_cpf, 'desconhecido')}.")
    else:
        print(f"O CPF número: {NOVO_CPF} é inválido, tente novamente.")


NOVO_CPF = input("Por favor digite seu cpf >>> ")
validacao_cpf(NOVO_CPF)
