import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []
imc = []
# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

#função calcular e mostrar a classificação
def calcular_imc (pesos, alturas):
   return peso / (altura ** 2)

def classificar_imc (imc):
    if imc < 18.5:
        classificar_imc = "abaixo do peso" 
    elif 18.5 <= imc < 25:
       classificar_imc = "peso normal"
    elif 25 <= imc < 30:
        classificar_imc= "sobrepeso"
    elif 30 <= imc < 35:
        classificar_imc= "obesidade grau 1"
    elif 35<= imc < 40:
        classificar_imc= "obesidade grau 2"
    elif imc >= 40:
        classificar_imc = "mórbida"
        return classificar_imc 


#exemplos de uso
peso =float (input("digite seu peso em quilogramas:"))
altura= float(input("digite sua altura em metros: "))

imc = calcular_imc (peso, altura)

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print(f"seu imc é: {imc:.2f}")
    print(f"classificação: {classificar_imc}")
