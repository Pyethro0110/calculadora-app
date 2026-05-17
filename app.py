import math

print("Olá, me chamo pi e sou sua calculadora.")

nome = input("Como se chama? ")
print("Olá", nome)

print("""
===== MENU =====
1 - Operações básicas
2 - Tabuada
3 - Equação do 2 grau
4 - Área
================
""")

opcao = input("Escolha uma opção (1-4): ")

# =======================
# 1 - OPERAÇÕES BÁSICAS
# =======================
if opcao == "1":

    n1 = float(input("Primeiro número: "))
    n2 = float(input("Segundo número: "))

    op = input("Escolha a operação (+ - * /): ")

    if op == "+":
        print("Resultado:", n1 + n2)

    elif op == "-":
        print("Resultado:", n1 - n2)

    elif op == "*":
        print("Resultado:", n1 * n2)

    elif op == "/":
        if n2 == 0:
            print("Não pode dividir por zero!")
        else:
            print("Resultado:", n1 / n2)

    else:
        print("Operação inválida.")


# =======================
# 2 - TABUADA
# =======================
elif opcao == "2":

    numero = int(input("Número: "))
    contador = 1

    while contador <= 10:
        print(numero, "x", contador, "=", numero * contador)
        contador += 1


# =======================
# 3 - EQUAÇÃO 2 GRAU
# =======================
elif opcao == "3":

    a = float(input("Informe o valor de A: "))
    b = float(input("Informe o valor de B: "))
    c = float(input("Informe o valor de C: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("Não existe raiz real.")

    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print("Solução: x1 =", x1, "x2 =", x2)


# =======================
# 4 - ÁREA
# =======================
elif opcao == "4":

    forma = input("Qual forma? (quadrado / retangulo / triangulo / circulo / trapezio / losango): ")

    if forma == "quadrado":
        lado = float(input("Lado: "))
        print("Área:", lado * lado)

    elif forma == "retangulo":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("Área:", base * altura)

    elif forma == "circulo":
        raio = float(input("Raio: "))
        print("Área:", math.pi * raio ** 2)

    elif forma == "triangulo":
        base = float(input("Base: "))
        altura = float(input("Altura: "))
        print("Área:", (base * altura) / 2)

    elif forma == "trapezio":
        B = float(input("Base maior: "))
        b = float(input("Base menor: "))
        h = float(input("Altura: "))
        print("Área:", (B + b) * h / 2)

    elif forma == "losango":
        D = float(input("Diagonal maior: "))
        d = float(input("Diagonal menor: "))
        print("Área:", (D * d) / 2)

    else:
        print("Forma inválida.")


# =======================
# ERRO
# =======================
else:
    print("Opção inválida. Escolha de 1 a 4.")
