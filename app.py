import streamlit as st
import math

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Super Calculadora",
    page_icon="🧮",
    layout="centered"
)

# HISTÓRICO
if "historico" not in st.session_state:
    st.session_state.historico = []

# TÍTULO
st.title("Super Calculadora")
st.write("Calculadora completa com várias funções")

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
        "Tabuada",
        "Conversor de Temperatura"
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
            st.session_state.historico.append(f"{a} + {b} = {resultado}")

    with col2:
        if st.button("Subtrair"):
            resultado = a - b
            st.session_state.historico.append(f"{a} - {b} = {resultado}")

    with col3:
        if st.button("Multiplicar"):
            resultado = a * b
            st.session_state.historico.append(f"{a} × {b} = {resultado}")

    with col4:
        if st.button("Dividir"):
            if b != 0:
                resultado = a / b
                st.session_state.historico.append(f"{a} ÷ {b} = {resultado}")
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
        st.session_state.historico.append(f"{base} ^ {expoente} = {resultado}")
        st.success(f"Resultado: {resultado}")

# =========================
# PORCENTAGEM
# =========================
elif opcao == "Porcentagem":

    valor = st.number_input("Valor", value=0.0)
    porcentagem = st.number_input("Porcentagem (%)", value=0.0)

    if st.button("Calcular Porcentagem"):
        resultado = (valor * porcentagem) / 100
        st.session_state.historico.append(f"{porcentagem}% de {valor} = {resultado}")
        st.success(f"Resultado: {resultado}")

# =========================
# RAIZ QUADRADA
# =========================
elif opcao == "Raiz Quadrada":

    numero = st.number_input("Digite um número", value=0.0)

    if st.button("Calcular Raiz"):
        if numero >= 0:
            resultado = math.sqrt(numero)
            st.session_state.historico.append(f"√{numero} = {resultado}")
            st.success(f"Resultado: {resultado}")
        else:
            st.error("Número negativo não possui raiz real.")

# =========================
# ÁREA
# =========================
elif opcao == "Área":

    figura = st.selectbox(
        "Escolha a figura:",
        [
            "Quadrado",
            "Retângulo",
            "Triângulo",
            "Círculo",
            "Losango",
            "Trapézio"
        ]
    )

    if figura == "Quadrado":

        lado = st.number_input("Lado", value=0.0)

        if st.button("Calcular Área"):
            area = lado * lado
            st.session_state.historico.append(f"Área quadrado: {area}")
            st.success(f"Área do quadrado: {area}")

    elif figura == "Retângulo":

        base = st.number_input("Base", value=0.0)
        altura = st.number_input("Altura", value=0.0)

        if st.button("Calcular Área"):
            area = base * altura
            st.session_state.historico.append(f"Área retângulo: {area}")
            st.success(f"Área do retângulo: {area}")

    elif figura == "Triângulo":

        base = st.number_input("Base", value=0.0)
        altura = st.number_input("Altura", value=0.0)

        if st.button("Calcular Área"):
            area = (base * altura) / 2
            st.session_state.historico.append(f"Área triângulo: {area}")
            st.success(f"Área do triângulo: {area}")

    elif figura == "Círculo":

        raio = st.number_input("Raio", value=0.0)

        if st.button("Calcular Área"):
            area = math.pi * (raio ** 2)
            st.session_state.historico.append(f"Área círculo: {area}")
            st.success(f"Área do círculo: {area:.2f}")

    elif figura == "Losango":

        dmaior = st.number_input("Diagonal maior", value=0.0)
        dmenor = st.number_input("Diagonal menor", value=0.0)

        if st.button("Calcular Área"):
            area = (dmaior * dmenor) / 2
            st.session_state.historico.append(f"Área losango: {area}")
            st.success(f"Área do losango: {area:.2f}")

    elif figura == "Trapézio":

        bmaior = st.number_input("Base maior", value=0.0)
        bmenor = st.number_input("Base menor", value=0.0)
        altura = st.number_input("Altura", value=0.0)

        if st.button("Calcular Área"):
            area = ((bmaior + bmenor) * altura) / 2
            st.session_state.historico.append(f"Área trapézio: {area}")
            st.success(f"Área do trapézio: {area:.2f}")

# =========================
# EQUAÇÃO DO 2º GRAU
# =========================
elif opcao == "Equação do 2º Grau":

    a = st.number_input("Valor de a", value=1.0)
    b = st.number_input("Valor de b", value=0.0)
    c = st.number_input("Valor de c", value=0.0)

    if st.button("Calcular Bhaskara"):

        if a == 0:
            st.error("O valor de 'a' não pode ser zero.")
        else:

            delta = (b ** 2) - (4 * a * c)

            if delta < 0:
                st.error("Sem raízes reais.")

            elif delta == 0:
                x = -b / (2 * a)
                st.session_state.historico.append(f"Bhaskara: x = {x}")
                st.success(f"x = {x}")

            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)

                st.session_state.historico.append(f"Bhaskara: x1={x1}, x2={x2}")
                st.success(f"x1 = {x1}, x2 = {x2}")

# =========================
# TABUADA
# =========================
elif opcao == "Tabuada":

    numero = st.number_input("Digite um número", value=1)

    if st.button("Gerar Tabuada"):

        for i in range(1, 11):
            st.write(f"{numero} x {i} = {numero*i}")

# =========================
# CONVERSOR DE TEMPERATURA
# =========================
elif opcao == "Conversor de Temperatura":

    temp = st.number_input("Temperatura", value=0.0)

    tipo = st.selectbox(
        "Converter:",
        ["Celsius → Fahrenheit", "Fahrenheit → Celsius", "Celsius → Kelvin"]
    )

    if st.button("Converter"):

        if tipo == "Celsius → Fahrenheit":
            resultado = (temp * 9/5) + 32

        elif tipo == "Fahrenheit → Celsius":
            resultado = (temp - 32) * 5/9

        else:
            resultado = temp + 273.15

        st.session_state.historico.append(f"Conversão: {resultado}")
        st.success(f"Resultado: {resultado:.2f}")

# =========================
# HISTÓRICO + LIMPAR
# =========================
st.markdown("---")
st.subheader("Histórico")

if st.session_state.historico:
    for item in st.session_state.historico[-10:]:
        st.write(item)
else:
    st.write("Sem histórico ainda.")

if st.button("Limpar histórico"):
    st.session_state.historico = []
    st.success("Histórico apagado!")

# RODAPÉ
st.markdown("---")
st.caption("FEITO POR PYHETR00")
