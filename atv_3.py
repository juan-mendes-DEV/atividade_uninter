# função da escolha de serviço
def escolha_servico(): 
    opcao_escolhida = ""
    print("Entre com o serviço desejado:\n")
    print("[DIG] para digitalização")
    print("[ICO] para impressão colorida")
    print("[IPB] para impressão preto e branco")
    print("[FOT] para fotocopia")
    # loop infinito ate determinada ação for feita
    while True:
        # tratamento de erros
        try:
            # obtendo a escolha do usuario e retornando
            escolha = input("qual serviço vc deseja contratar? [DIG] [ICO] [IPB] ou [FOT]\n-").upper()
            if escolha == "DIG":
                print("o custo por página é de um real e dez centavos")
                return escolha
            elif escolha == "ICO":
                print("o custo por página é de um real")
                opcao_escolhida = escolha
                return escolha
            elif escolha == "IPB":
                print("o custo por página é de quarenta centavos")
                opcao_escolhida = escolha
                return escolha
            elif escolha == "FOT":
                print("o custo por página é de vinte centavos")
                opcao_escolhida = escolha
                return escolha
            else:
                print("escolha invalida tente novamente")
        
        # caso aconteça algum erro
        except Exception as e:
            print(f"Ocorreu um erro ao escolher o serviço: {e}. Tente novamente.\n")
# função de numero de paginas'
def num_pagina():
    # obtendo o serviço escolhido na funcao anterior para soma e aplicação do desconto
    servico = escolha_servico()
    print(f"voce escolheu o servico: {servico}\n")
    
    # loop infinito ate determinada ação for feita
    while True:
        try:
            # obtendo a quantidade de pagina para aplicação do desconto
            numero_pag = input("qual a quantidade de paginas desejada?")

            if numero_pag.isdigit():
                # transformando o numero em inteiro para a conta
                numero_pag = int(numero_pag)

                if numero_pag > 20000:
                    print("Número de páginas muito alto!")
                else:
                    if servico == "DIG":
                        
                        preco_por_pagina = 1.10  # Preço fixo por página
                        n1 = numero_pag * preco_por_pagina  # Calcula o valor total sem desconto

                        if numero_pag < 20:
                            print("não a desconto\n")
                            conta_final = numero_pag * 1.10
                            return conta_final

                        elif numero_pag >= 20 and numero_pag < 200:
                            desconto = 0.15 
                            conta_final = n1 * (1 - desconto)

                        elif numero_pag >= 200 and numero_pag < 2000:
                            desconto = 0.20
                            conta_final = n1 * (1 - desconto)

                        elif numero_pag >= 2000 and numero_pag < 20000:
                            desconto = 0.25 
                            conta_final = n1 * (1 - desconto)

                        else:
                            print("não e aceito esta quantidade de paginas\n")
                            return None

                        if numero_pag >= 20:
                            print(f"Desconto aplicado: R$ {n1 * desconto:.2f} \n")
        
                        print(f"Valor final após desconto: R$ {conta_final:.2f} \n")
                        return conta_final

                    elif servico == "ICO":
                        
                        preco_por_pagina = 1  # Preço fixo por página
                        n1 = numero_pag * preco_por_pagina  # Calcula o valor total sem desconto

                        if numero_pag < 20:
                            print("não a desconto\n")
                            conta_final = numero_pag * 1
                            return conta_final

                        elif numero_pag >= 20 and numero_pag < 200:
                            desconto = 0.15 
                            conta_final = n1 * (1 - desconto)

                        elif numero_pag >= 200 and numero_pag < 2000:
                            desconto = 0.20
                            conta_final = n1 * (1 - desconto)

                        elif numero_pag >= 2000 and numero_pag < 20000:
                            desconto = 0.25 
                            conta_final = n1 * (1 - desconto)

                        else:
                            print("não e aceito esta quantidade de paginas\n")
                            return None

                        if numero_pag >= 20:
                            print(f"Desconto aplicado: R$ {n1 * desconto:.2f}\n")
        
                        print(f"Valor final após desconto: R$ {conta_final:.2f}\n")
                        return conta_final

                    elif servico == "IPB":
                        
                        preco_por_pagina = 0.40  # Preço fixo por página
                        n1 = numero_pag * preco_por_pagina  # Calcula o valor total sem desconto

                        if numero_pag < 20:
                            print("não a desconto \n")
                            conta_final = numero_pag * 0.40
                            return conta_final

                        elif numero_pag >= 20 and numero_pag < 200:
                            desconto = 0.15 
                            conta_final = n1 * (1 - desconto)

                        elif numero_pag >= 200 and numero_pag < 2000:
                            desconto = 0.20
                            conta_final = n1 * (1 - desconto)

                        elif numero_pag >= 2000 and numero_pag < 20000:
                            desconto = 0.25 
                            conta_final = n1 * (1 - desconto)

                        else:
                            print("não e aceito esta quantidade de paginas \n")
                            return None

                        if numero_pag >= 20:
                            print(f"Desconto aplicado: R$ {n1 * desconto:.2f}\n")
        
                        print(f"Valor final após desconto: R$ {conta_final:.2f}\n")
                        return conta_final

                    elif servico == "FOT":
                        
                        preco_por_pagina = 0.20  # Preço fixo por página
                        n1 = numero_pag * preco_por_pagina  # Calcula o valor total sem desconto

                        if numero_pag < 20:
                            print("não a desconto\n")
                            conta_final = numero_pag * 0.20
                            return conta_final

                        elif numero_pag >= 20 and numero_pag < 200:
                            desconto = 0.15 
                            conta_final = n1 * (1 - desconto)

                        elif numero_pag >= 200 and numero_pag < 2000:
                            desconto = 0.20
                            conta_final = n1 * (1 - desconto)

                        elif numero_pag >= 2000 and numero_pag < 20000:
                            desconto = 0.25 
                            conta_final = n1 * (1 - desconto)

                        else:
                            print("não e aceito esta quantidade de paginas\n")
                            return None

                        if numero_pag >= 20:
                            print(f"Desconto aplicado: R$ {n1 * desconto:.2f}\n")
        
                        print(f"Valor final após desconto: R$ {conta_final:.2f}\n")
                        return conta_final
                    
                
            else:
                print("Por favor, insira um número válido.\n")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.\n")
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Tente novamente.\n")

# função de mais serviços que sera cobrado adicional do cliente
def servico_adicional(quantidade_num_pagina):
    # loop e tratamento de erros
    while True:
        try:
            print("de encadernação simples (1) é cobrado um valor extra de 15 reais\n")
            print("de encadernação de capa dura (2) é cobrado um valor extra de 40 reais\n")
            print("de não querer mais nada (0) é cobrado um valor extra de 0 reais")
            escolha = input("voce deseja algum serviço adicional? \n")
            total = quantidade_num_pagina

            if(escolha == "1"):
                total += 15 
                print(f"o valor total a pagar é: {total}")
                return total
            elif(escolha == "2"):
                total += 40
                print(f"o valor total a pagar é: {total}")
                return total
            elif(escolha == "0"):
                total += 0
                print(f"o valor total a pagar é: {total}")
                return total
            else:
                break

        except Exception as e:
            print(f"Ocorreu um erro ao processar o serviço adicional: {e}. Tente novamente.\n")
# funçao principal aonde tudo é execu'tado
def main():
    print("para continuar digite seu nome e sobrenome")
    # obtendo nomes
    nome = input("digite seu nome: ")
    sobrenome = input("digite seu sobrenome: ")

    print(f"ola {nome} {sobrenome} seja bem vindo a copiadora. ;D\n\n")

    quantidade_num_pagina = num_pagina()
    servico_adicional(quantidade_num_pagina)

# chamada da função principal
main()

