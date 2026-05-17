import streamlit as st
import math

st.set_page_config(
    page_title="Super Calculadora Pro",
    layout="centered"
)

# TEMA VISUAL FORTE
st.markdown("""
<style>

body {
    background-color: #0b0f19;
}

.stApp {
    background-color: #0b0f19;
    color: #ffffff;
}

h1, h2, h3 {
    color: #ffffff;
    text-align: center;
}

/* INPUTS */
input {
    background-color: #151a2b !important;
    color: white !important;
    border-radius: 10px !important;
}

/* BOTÕES */
.stButton>button {
    width: 100%;
    height: 55px;
    font-size: 16px;
    border-radius: 12px;
    border: none;
    background: linear-gradient(135deg, #4c5cff, #7c3aed);
    color: white;
    font-weight: bold;
    transition: 0.2s;
}

.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(135deg, #6d28d9, #2563eb);
}

/* CAIXAS */
.block-container {
    padding-top: 2rem;
}

div[data-testid="stSelectbox"] {
    background-color: #151a2b;
    border-radius: 10px;
    padding: 5px;
}

</style>
""", unsafe_allow_html=True)

# HISTÓRICO
if "historico" not in st.session_state:
    st.session_state.historico = []

st.title("Super Calculadora Pro")

opcao = st.selectbox(
    "Escolha uma função",
    [
        "Básico",
        "Potência",
        "Porcentagem",
        "Raiz",
        "Área",
        "Bhaskara",
        "Tabuada",
        "Temperatura"
    ]
)

st.markdown("---")

# =====================
# BÁSICO
# =====================
if opcao == "Básico":

    a = st.number_input("Número A", value=0.0)
    b = st.number_input("Número B", value=0.0)

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    if col1.button("Somar"):
        r = a + b
        st.session_state.historico.append(f"{a}+{b}={r}")
        st.success(r)

    if col2.button("Subtrair"):
        r = a - b
        st.session_state.historico.append(f"{a}-{b}={r}")
        st.success(r)

    if col3.button("Multiplicar"):
        r = a * b
        st.session_state.historico.append(f"{a}×{b}={r}")
        st.success(r)

    if col4.button("Dividir"):
        if b != 0:
            r = a / b
            st.session_state.historico.append(f"{a}/{b}={r}")
            st.success(r)
        else:
            st.error("Erro divisão por zero")

# =====================
# POTÊNCIA
# =====================
elif opcao == "Potência":

    base = st.number_input("Base", value=0.0)
    exp = st.number_input("Expoente", value=0.0)

    if st.button("Calcular"):
        r = base ** exp
        st.session_state.historico.append(f"{base}^{exp}={r}")
        st.success(r)

# =====================
# PORCENTAGEM
# =====================
elif opcao == "Porcentagem":

    v = st.number_input("Valor", value=0.0)
    p = st.number_input("Porcentagem", value=0.0)

    if st.button("Calcular"):
        r = (v * p) / 100
        st.session_state.historico.append(f"{p}% de {v}={r}")
        st.success(r)

# =====================
# RAIZ
# =====================
elif opcao == "Raiz":

    n = st.number_input("Número", value=0.0)

    if st.button("Calcular"):
        if n >= 0:
            r = math.sqrt(n)
            st.session_state.historico.append(f"√{n}={r}")
            st.success(r)
        else:
            st.error("Número negativo não possui raiz real")

# =====================
# ÁREA
# =====================
elif opcao == "Área":

    fig = st.selectbox("Figura", ["Quadrado", "Retângulo", "Círculo"])

    if fig == "Quadrado":
        l = st.number_input("Lado", value=0.0)
        if st.button("Calcular"):
            r = l * l
            st.session_state.historico.append(f"Quadrado={r}")
            st.success(r)

    if fig == "Retângulo":
        b = st.number_input("Base", value=0.0)
        h = st.number_input("Altura", value=0.0)
        if st.button("Calcular"):
            r = b * h
            st.session_state.historico.append(f"Retângulo={r}")
            st.success(r)

    if fig == "Círculo":
        r0 = st.number_input("Raio", value=0.0)
        if st.button("Calcular"):
            r = math.pi * r0 ** 2
            st.session_state.historico.append(f"Círculo={r}")
            st.success(round(r, 2))

# =====================
# BHASKARA
# =====================
elif opcao == "Bhaskara":

    a = st.number_input("a", value=1.0)
    b = st.number_input("b", value=0.0)
    c = st.number_input("c", value=0.0)

    if st.button("Resolver"):

        d = b**2 - 4*a*c

        if d < 0:
            st.error("Sem raízes reais")
        else:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)

            st.session_state.historico.append(f"x1={x1}, x2={x2}")
            st.success(f"x1={x1} | x2={x2}")

# =====================
# TABUADA
# =====================
elif opcao == "Tabuada":

    n = st.number_input("Número", value=1)

    if st.button("Gerar"):
        for i in range(1, 11):
            st.write(f"{n} x {i} = {n*i}")

# =====================
# TEMPERATURA
# =====================
elif opcao == "Temperatura":

    t = st.number_input("Temperatura", value=0.0)

    tipo = st.selectbox(
        "Converter",
        ["C → F", "F → C", "C → K"]
    )

    if st.button("Converter"):

        if tipo == "C → F":
            r = (t * 9/5) + 32
        elif tipo == "F → C":
            r = (t - 32) * 5/9
        else:
            r = t + 273.15

        st.session_state.historico.append(f"Temp={r}")
        st.success(round(r, 2))

# =====================
# HISTÓRICO
# =====================
st.markdown("---")
st.subheader("Histórico")

if st.button("Limpar histórico"):
    st.session_state.historico = []

for item in st.session_state.historico[-8:]:
    st.write("•", item)
