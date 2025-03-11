# Mensagem de boas-vindas com nome e sobrenome
print("Para continuar, digite seu nome e sobrenome.")
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")

print(f"Olá {nome} {sobrenome}, seja bem-vindo à minha loja de Açaí e Cupuaçu! \n")

acpequeno = 11
acmedio = 16 
acgrande = 20
    
cppequeno = 9
cpmedio = 14 
cpgrande = 18

total = 0  

while True:
    # Escolher o sabor / se a opção for incorreta continua neste loop
    while True:
        escolha = input("O que deseja? Para açai digite [AC], para Cupuaçu digite [CP]: ").upper()
        if escolha == "AC":
            tamanho = input("Qual tamanho deseja? [P] Pequeno | [M] Médio | [G] Grande: ").upper()
            if tamanho == "P":
                total += acpequeno
                print("voce pediu um acai do tamanho pequeno")
                break
            elif tamanho == "M":
                total += acmedio
                print("voce pediu um acai do tamanho medio")
                break
            elif tamanho == "G":
                print("voce pediu um acai do tamanho grande")
                total += acgrande
                break
            else:
                print("Tamanho inválido. Tente novamente.")
                continue
                break
        elif escolha == "CP":
            tamanho = input("Qual tamanho deseja? [P] Pequeno | [M] Médio | [G] Grande: ").upper()
            if tamanho == "P":
                # adicionando ao acumulador
                total += cppequeno
                print("voce pediu um cupuacu do tamanho pequeno")
                break
            elif tamanho == "M":
                total += cpmedio
                print("voce pediu um cupuacu do tamanho medio")
                break
            elif tamanho == "G":
                print("voce pediu um cupuacu do tamanho grande")
                total += cpgrande
                break
            else:
                print("Tamanho inválido. Tente novamente.")
                continue
                break
        else:
            print("Sabor inválido. Tente novamente.")
            continue
    
    preco = total
    print(f"Pedido adicionado: {escolha} tamanho {tamanho} - R$ {preco:.2f}\n")

    # Perguntando se deseja continuar se sim ele vai add e somando até a pessoa sair, aí sai o valor total
    continuar = input("Deseja pedir mais alguma coisa? [S/N]: ").upper()
    if continuar == "S":
        continue
    elif continuar == "N":
        break  # Sai do loop se a resposta for não
    else:
        print("opção invalida digite novamente...")
# Exibe o total da compra, formatando o preço
print(f"\nTotal da sua compra: R$ {total:.2f}")
