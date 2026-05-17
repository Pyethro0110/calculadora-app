import streamlit as st
import math

st.set_page_config(
    page_title="calculadora-app",
    layout="centered"
)

# =========================
# ESTADO
# =========================
if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# ESTILO SIMPLES
# =========================
st.markdown("""
<style>

.stApp {
    background: #f8fafc;
    color: #111827;
    font-family: Arial, sans-serif;
}

/* TÍTULO */
.title {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: #0ea5e9;
    margin-bottom: 5px;
}

/* ASSINATURA */
.footer {
    margin-top: 30px;
    text-align: center;
    font-size: 12px;
    color: #64748b;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO
# =========================
st.markdown('<div class="title">calculadora-app</div>', unsafe_allow_html=True)

st.write("Escolha uma função no menu abaixo")

# =========================
# MENU
# =========================
opcao = st.selectbox(
    "Menu",
    [
        "Operações Básicas",
        "Potência",
        "Porcentagem",
        "Raiz Quadrada",
        "Logaritmo",
        "Conversor de Temperatura",
        "Conversor de Medidas",
        "Bhaskara",
        "IMC",
        "Histórico"
    ]
)

st.markdown("---")

# =========================
# OPERAÇÕES BÁSICAS
# =========================
if opcao == "Operações Básicas":

    a = st.number_input("Número 1", value=0.0)
    b = st.number_input("Número 2", value=0.0)
    operacao = st.selectbox("Operação", ["+", "-", "*", "/"])

    if st.button("Calcular"):

        if operacao == "+":
            r = a + b
        elif operacao == "-":
            r = a - b
        elif operacao == "*":
            r = a * b
        elif operacao == "/":
            r = a / b if b != 0 else "Erro divisão por zero"

        st.session_state.history.append(f"{a} {operacao} {b} = {r}")
        st.success(r)

# =========================
# POTÊNCIA
# =========================
elif opcao == "Potência":

    base = st.number_input("Base", value=0.0)
    exp = st.number_input("Expoente", value=0.0)

    if st.button("Calcular"):
        r = base ** exp
        st.session_state.history.append(f"{base}^{exp} = {r}")
        st.success(r)

# =========================
# PORCENTAGEM
# =========================
elif opcao == "Porcentagem":

    valor = st.number_input("Valor", value=0.0)
    porc = st.number_input("Porcentagem (%)", value=0.0)

    if st.button("Calcular"):
        r = (valor * porc) / 100
        st.session_state.history.append(f"{porc}% de {valor} = {r}")
        st.success(r)

# =========================
# RAIZ QUADRADA
# =========================
elif opcao == "Raiz Quadrada":

    n = st.number_input("Número", value=0.0)

    if st.button("Calcular"):
        if n >= 0:
            r = math.sqrt(n)
        else:
            r = "Número inválido"

        st.session_state.history.append(f"√{n} = {r}")
        st.success(r)

# =========================
# LOGARITMO
# =========================
elif opcao == "Logaritmo":

    n = st.number_input("Número", value=1.0)

    if st.button("Calcular"):
        if n > 0:
            r = math.log10(n)
        else:
            r = "Inválido"

        st.session_state.history.append(f"log({n}) = {r}")
        st.success(r)

# =========================
# TEMPERATURA
# =========================
elif opcao == "Conversor de Temperatura":

    t = st.number_input("Temperatura", value=0.0)
    tipo = st.selectbox("Conversão", ["C → F", "F → C", "C → K"])

    if st.button("Converter"):

        if tipo == "C → F":
            r = (t * 9/5) + 32
        elif tipo == "F → C":
            r = (t - 32) * 5/9
        else:
            r = t + 273.15

        st.session_state.history.append(f"{t} {tipo} = {r}")
        st.success(r)

# =========================
# MEDIDAS
# =========================
elif opcao == "Conversor de Medidas":

    m = st.number_input("Metros", value=1.0)

    if st.button("Converter"):
        r = m * 100
        st.session_state.history.append(f"{m} m = {r} cm")
        st.success(f"{r} cm")

# =========================
# BHASKARA
# =========================
elif opcao == "Bhaskara":

    a = st.number_input("a", value=1.0)
    b = st.number_input("b", value=0.0)
    c = st.number_input("c", value=0.0)

    if st.button("Resolver"):

        delta = b**2 - 4*a*c

        if delta < 0:
            r = "Sem raízes reais"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            r = f"x1={x1}, x2={x2}"

        st.session_state.history.append(f"Bhaskara: {r}")
        st.success(r)

# =========================
# IMC
# =========================
elif opcao == "IMC":

    peso = st.number_input("Peso (kg)", value=70.0)
    altura = st.number_input("Altura (m)", value=1.70)

    if st.button("Calcular"):
        r = peso / (altura**2)
        st.session_state.history.append(f"IMC = {r}")
        st.success(round(r, 2))

# =========================
# HISTÓRICO
# =========================
elif opcao == "Histórico":

    st.subheader("Histórico de cálculos")

    if st.button("Limpar histórico"):
        st.session_state.history = []

    for item in st.session_state.history[-15:]:
        st.write(item)

# =========================
# RODAPÉ (SUA ASSINATURA)
# =========================
st.markdown("""
<div class="footer">
FEITO POR PYHETR00
</div>
""", unsafe_allow_html=True)
