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

if "expr" not in st.session_state:
    st.session_state.expr = ""

# =========================
# ESTILO MODERNO (BASE LIMPA)
# =========================
st.markdown("""
<style>

/* FUNDO LIMPO MODERNO */
.stApp {
    background: #f8fafc;
    color: #111827;
    font-family: Arial, sans-serif;
}

/* TÍTULO RETRÔ PIXEL AZUL */
.title-retro {
    text-align: center;
    font-size: 34px;
    font-weight: 700;
    color: #38bdf8;

    /* efeito pixel/neon */
    text-shadow:
        1px 1px 0px #0ea5e9,
        2px 2px 0px #0284c7,
        3px 3px 0px #0369a1;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

/* DISPLAY MODERNO */
.display {
    background: white;
    border-radius: 12px;
    padding: 18px;
    font-size: 30px;
    text-align: right;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    margin-bottom: 12px;
}

/* BOTÕES MODERNOS */
.stButton>button {
    border-radius: 10px;
    height: 50px;
    font-size: 16px;
}

/* HISTÓRICO */
.history {
    margin-top: 10px;
    padding: 10px;
    background: #f1f5f9;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TÍTULO (SÓ AQUI É RETRÔ)
# =========================
st.markdown("""
<div class="title-retro">
calculadora-app
</div>
""", unsafe_allow_html=True)

# =========================
# FUNÇÕES
# =========================
def add(v):
    st.session_state.expr += str(v)

def clear():
    st.session_state.expr = ""

def calc(expr):
    try:
        return eval(expr, {"__builtins__": None}, {})
    except:
        return "erro"

# =========================
# DISPLAY
# =========================
st.markdown(f"""
<div class="display">
{st.session_state.expr or "0"}
</div>
""", unsafe_allow_html=True)

# =========================
# TECLADO SIMPLES
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.button("C", on_click=clear)
col2.button("7", on_click=lambda: add("7"))
col3.button("8", on_click=lambda: add("8"))
col4.button("9", on_click=lambda: add("9"))

col1, col2, col3, col4 = st.columns(4)

col1.button("4", on_click=lambda: add("4"))
col2.button("5", on_click=lambda: add("5"))
col3.button("6", on_click=lambda: add("6"))
col4.button("+", on_click=lambda: add("+"))

col1, col2, col3, col4 = st.columns(4)

col1.button("1", on_click=lambda: add("1"))
col2.button("2", on_click=lambda: add("2"))
col3.button("3", on_click=lambda: add("3"))
col4.button("-", on_click=lambda: add("-"))

col1, col2, col3, col4 = st.columns(4)

col1.button("0", on_click=lambda: add("0"))
col2.button(".", on_click=lambda: add("."))

if col3.button("="):
    r = calc(st.session_state.expr)
    st.session_state.history.append(f"{st.session_state.expr} = {r}")
    st.session_state.expr = str(r)

col4.button("÷", on_click=lambda: add("/"))

# =========================
# HISTÓRICO
# =========================
st.markdown("---")
st.subheader("history")

if st.button("clear history"):
    st.session_state.history = []

for item in st.session_state.history[-10:]:
    st.write(item)
