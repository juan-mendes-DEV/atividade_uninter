print("para continuar digite seu nome e sobrenome:")
# obtendo os nomes para a saudação
nome = input("digite seu nome: ")
sobrenome = input("digite seu sobrenome: ")

print(f"\nola {nome} {sobrenome} seja bem vindo a meu primeiro trabalho da uninter sobre vendas!! ;D\n")
print("--------------------------------")
print("| escolha seu livro e quantidade: |")
print("--------------------------------\n")
print("livros disponiveis: \n")
print("para harry potter digite [1], preço R$100,00 ")
print("para senhor dos aneis [2], preço R$70,00\n")

# obtem o livro escolhido 
escolha_livro = input("\nqual livro deseja comprar? ")
qtd_livro = input("quantidade de livros desejada? ")
    
# aqui é feito a conta da aplicação do desconto
if escolha_livro == "1":
    print("o livro escolhido foi harry potter")
    n1 = int(qtd_livro) * 100

    if n1  < 2500:
        print(f"valor sem desconto: {n1}")
    elif n1 >= 2500 and n1 < 6000:
        desconto = 0.04
        conta = n1 * desconto
        valor_final = n1 - conta
        print(f"o desconto foi de: R${conta}")
        print(f"o valor sem desconto é R${n1}")
        print(f"e o valor final é: R${valor_final}")
    elif n1 >= 6000 and n1 < 10000:
        desconto = 0.07
        conta = n1 * desconto
        valor_final = n1 - conta
        print(f"o desconto foi de: R${conta}")
        print(f"o valor sem desconto é R${n1}")
        print(f"e o valor final é: R${valor_final}")
    elif n1 >= 10000:
        desconto = 0.11
        conta = n1 * desconto
        valor_final = n1 - conta
        print(f"o desconto foi de: R${conta}")
        print(f"o valor sem desconto é R${n1}")
        print(f"e o valor final é: R${valor_final}")
    else:
        print("error tente novamente")
elif escolha_livro == "2":
    print("o livro escolhido foi senhor dos aneis")
    n1 = int(qtd_livro) * 70

    if n1  < 2500:
        print(f"esse valor não possui desconto: {n1}")
    elif n1 >= 2500 and n1 < 6000:
        desconto = 0.04
        conta = n1 * desconto
        valor_final = n1 - conta
        print(f"o desconto foi de: R${conta}")
        print(f"o valor sem desconto é R${n1}")
        print(f"e o valor final é: R${valor_final}")
    elif n1 >= 6000 and n1 < 10000:
        desconto = 0.07
        conta = n1 * desconto
        valor_final = n1 - conta
        print(f"o desconto foi de: R${conta}")
        print(f"o valor sem desconto é R${n1}")
        print(f"e o valor final é: R${valor_final}")
    elif n1 >= 10000:
        desconto = 0.11
        conta = n1 * desconto
        valor_final = n1 - conta
        print(f"o desconto foi de: R${conta}")
        print(f"o valor sem desconto é R${n1}")
        print(f"e o valor final é: R${valor_final}")
    else:
        print("error tente novamente")
else:
    print("error tente novamente!!")
    

