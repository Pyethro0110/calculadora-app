import streamlit as st
import math

st.set_page_config(
    page_title="Calculadora Pro Max",
    layout="centered"
)

# =========================
# ESTILO VISUAL AVANÇADO
# =========================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #0f1220, #070912);
    color: white;
}

/* TÍTULO */
h1 {
    text-align: center;
    font-size: 38px;
}

/* BOTÕES MODERNOS */
.stButton>button {
    width: 100%;
    height: 65px;
    border-radius: 18px;
    border: none;
    background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    color: white;
    font-size: 18px;
    font-weight: bold;
    transition: all 0.2s ease-in-out;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
}

.stButton>button:hover {
    transform: translateY(-3px) scale(1.02);
    background: linear-gradient(135deg, #2563eb, #7c3aed);
}

/* INPUTS */
input {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 12px !important;
}

/* SELECT */
div[data-testid="stSelectbox"] {
    background-color: #111827;
    border-radius: 12px;
    padding: 5px;
}

/* HISTÓRICO */
.history {
    background-color: #0b1020;
    padding: 12px;
    border-radius: 12px;
    margin-top: 10px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
}

</style>
""", unsafe_allow_html=True)

# =========================
# ESTADO
# =========================
if "historico" not in st.session_state:
    st.session_state.historico = []

# =========================
# TÍTULO
# =========================
st.title("Calculadora Pro Max")

# =========================
# MENU
# =========================
opcao = st.selectbox(
    "Escolha uma função",
    [
        "Básico",
        "Potência",
        "Porcentagem",
        "Raiz",
        "Fatorial",
        "Logaritmo",
        "Bhaskara",
        "Tabuada",
        "Temperatura",
        "IMC"
    ]
)

st.markdown("---")

# =========================
# BÁSICO (LAYOUT TIPO PAINEL)
# =========================
if opcao == "Básico":

    a = st.number_input("Número A", value=0.0)
    b = st.number_input("Número B", value=0.0)

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("+"):
        r = a + b
        st.session_state.historico.append(f"{a}+{b}={r}")
        st.success(r)

    if col2.button("-"):
        r = a - b
        st.session_state.historico.append(f"{a}-{b}={r}")
        st.success(r)

    if col3.button("×"):
        r = a * b
        st.session_state.historico.append(f"{a}×{b}={r}")
        st.success(r)

    if col4.button("÷"):
        if b != 0:
            r = a / b
            st.session_state.historico.append(f"{a}/{b}={r}")
            st.success(r)
        else:
            st.error("Divisão por zero")

# =========================
# POTÊNCIA
# =========================
elif opcao == "Potência":
    x = st.number_input("Base", value=0.0)
    y = st.number_input("Expoente", value=0.0)

    if st.button("Calcular"):
        r = x ** y
        st.session_state.historico.append(f"{x}^{y}={r}")
        st.success(r)

# =========================
# PORCENTAGEM
# =========================
elif opcao == "Porcentagem":
    v = st.number_input("Valor", value=0.0)
    p = st.number_input("Percentual", value=0.0)

    if st.button("Calcular"):
        r = (v * p) / 100
        st.session_state.historico.append(f"{p}% de {v}={r}")
        st.success(r)

# =========================
# RAIZ
# =========================
elif opcao == "Raiz":
    n = st.number_input("Número", value=0.0)

    if st.button("Calcular"):
        if n >= 0:
            r = math.sqrt(n)
            st.session_state.historico.append(f"√{n}={r}")
            st.success(r)
        else:
            st.error("Número inválido")

# =========================
# FATORIAL (NOVA FUNÇÃO)
# =========================
elif opcao == "Fatorial":
    n = st.number_input("Número inteiro", value=1, step=1)

    if st.button("Calcular"):
        r = math.factorial(int(n))
        st.session_state.historico.append(f"{n}!={r}")
        st.success(r)

# =========================
# LOGARITMO (NOVA FUNÇÃO)
# =========================
elif opcao == "Logaritmo":
    n = st.number_input("Número", value=1.0)

    if st.button("Calcular"):
        if n > 0:
            r = math.log10(n)
            st.session_state.historico.append(f"log({n})={r}")
            st.success(r)
        else:
            st.error("Número inválido")

# =========================
# BHASKARA
# =========================
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

# =========================
# TABUADA
# =========================
elif opcao == "Tabuada":
    n = st.number_input("Número", value=1)

    if st.button("Gerar"):
        for i in range(1, 11):
            st.write(f"{n} x {i} = {n*i}")

# =========================
# TEMPERATURA
# =========================
elif opcao == "Temperatura":
    t = st.number_input("Temperatura", value=0.0)

    tipo = st.selectbox(
        "Converter",
        ["C → F", "F → C", "C → K"]
    )

    if st.button("Converter"):

        if tipo == "C → F":
            r = (t*9/5)+32
        elif tipo == "F → C":
            r = (t-32)*5/9
        else:
            r = t + 273.15

        st.session_state.historico.append(f"Temp={r}")
        st.success(r)

# =========================
# IMC (NOVA FUNÇÃO)
# =========================
elif opcao == "IMC":
    peso = st.number_input("Peso (kg)", value=70.0)
    altura = st.number_input("Altura (m)", value=1.70)

    if st.button("Calcular"):
        r = peso / (altura ** 2)
        st.session_state.historico.append(f"IMC={r}")
        st.success(round(r, 2))

# =========================
# HISTÓRICO
# =========================
st.markdown("---")
st.subheader("Histórico")

if st.button("Limpar histórico"):
    st.session_state.historico = []

st.markdown('<div class="history">', unsafe_allow_html=True)

for item in st.session_state.historico[-10:]:
    st.write(item)

st.markdown('</div>', unsafe_allow_html=True)
