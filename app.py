import streamlit as st
import math

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Super Calculadora",
    page_icon="🧮",
    layout="centered"
)

# TÍTULO
st.title("Super Calculadora")
st.write("Calculadora completa com várias funções ")

# MENU
opcao = st.selectbox(
    "Escolha uma função:",
    [
        "Operações Básicas",
        "Potência",
        "Porcentagem",
        "Raiz Quadrada",
        "Área",
        "Equação do 2º Grau",
        "Tabuada"
    ]
)

st.markdown("---")

# =========================
# OPERAÇÕES BÁSICAS
# =========================
if opcao == "Operações Básicas":

    a = st.number_input("Primeiro número", value=0.0)
    b = st.number_input("Segundo número", value=0.0)

    col1, col2, col3, col4 = st.columns(4)

    resultado = None

    with col1:
        if st.button("Somar"):
            resultado = a + b

    with col2:
        if st.button("Subtrair"):
            resultado = a - b

    with col3:
        if st.button("Multiplicar"):
            resultado = a * b

    with col4:
        if st.button("Dividir"):
            if b != 0:
                resultado = a / b
            else:
                resultado = "Erro: divisão por zero"

    if resultado is not None:
        st.success(f"Resultado: {resultado}")

# =========================
# POTÊNCIA
# =========================
elif opcao == "Potência":

    base = st.number_input("Base", value=0.0)
    expoente = st.number_input("Expoente", value=0.0)

    if st.button("Calcular Potência"):
        resultado = base ** expoente
        st.success(f"Resultado: {resultado}")

# =========================
# PORCENTAGEM
# =========================
elif opcao == "Porcentagem":

    valor = st.number_input("Valor", value=0.0)
    porcentagem = st.number_input("Porcentagem (%)", value=0.0)

    if st.button("Calcular Porcentagem"):
        resultado = (valor * porcentagem) / 100
        st.success(f"Resultado: {resultado}")

# =========================
# RAIZ QUADRADA
# =========================
elif opcao == "Raiz Quadrada":

    numero = st.number_input("Digite um número", value=0.0)

    if st.button("Calcular Raiz"):
        if numero >= 0:
            resultado = math.sqrt(numero)
            st.success(f"Resultado: {resultado}")
        else:
            st.error("Número negativo não possui raiz real.")

# =========================
# ÁREA
# =========================
elif opcao == "Área":

    figura = st.selectbox(
        "Escolha a figura:",
        ["Quadrado", "Retângulo", "Triângulo", "Círculo", "Losango", "Trapézio"]
    )

    if figura == "Quadrado":

        lado = st.number_input("Lado", value=0.0)

        if st.button("Calcular Área"):
            area = lado * lado
            st.success(f"Área do quadrado: {area}")

    elif figura == "Retângulo":

        base = st.number_input("Base", value=0.0)
        altura = st.number_input("Altura", value=0.0)

        if st.button("Calcular Área"):
            area = base * altura
            st.success(f"Área do retângulo: {area}")

    elif figura == "Triângulo":

        base = st.number_input("Base", value=0.0)
        altura = st.number_input("Altura", value=0.0)

        if st.button("Calcular Área"):
            area = (base * altura) / 2
            st.success(f"Área do triângulo: {area}")

    elif figura == "Círculo":

        raio = st.number_input("Raio", value=0.0)

        if st.button("Calcular Área"):
            area = math.pi * (raio ** 2)
            st.success(f"Área do círculo: {area:.2f}")

elif figura == "Losango":

    diagonal_maior = st.number_input("Diagonal maior", value=0,0)
    diagonal_menor = st.number_input("Diagonal menor", value=0,0)

    if st.button("Calcular Área"):
        area = (diagonal_maior * diagonal_menor) / 2
        st.sucess(f"Área do losango: {area:.2f}")

elif figura == "Trapézio":

    base_maior = st.number_input("Base maior", value=0,0)
    base_menor = st.number_input("Base menor", value=0,0)
    altura = st.number_input("Altura", value=0,0)
    
   if st.button("Calcular Área"):
       area = (base_maior + base_menor) * altura / 2
    st.sucess("Área do trapézio: {area}")

# =========================
# EQUAÇÃO DO 2º GRAU
# =========================
elif opcao == "Equação do 2º Grau":

    st.write("Equação: ax² + bx + c = 0")

    a = st.number_input("Valor de a", value=1.0)
    b = st.number_input("Valor de b", value=0.0)
    c = st.number_input("Valor de c", value=0.0)

    if st.button("Resolver Equação"):

        delta = (b ** 2) - (4 * a * c)

        st.write(f"Delta = {delta}")

        if delta < 0:
            st.error("A equação não possui raízes reais.")

        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

            st.success(f"x1 = {x1}")
            st.success(f"x2 = {x2}")

# =========================
# TABUADA
# =========================
elif opcao == "Tabuada":

    numero = st.number_input("Digite um número", value=1)

    if st.button("Gerar Tabuada"):

        st.subheader(f"Tabuada do {numero}")

        for i in range(1, 11):
            resultado = numero * i
            st.write(f"{numero} x {i} = {resultado}")

# RODAPÉ
st.markdown("---")
st.caption("FEITO POR PYHETR00")
