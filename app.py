import streamlit as st
import math
import re

st.set_page_config(
    page_title="Calculadora Pro",
    layout="centered"
)

# =========================
# CSS FORÇADO (RESPONSIVO FIXO)
# =========================
st.markdown("""
<style>

.stApp {
    background: #0b0f1a;
    color: white;
}

/* CENTRALIZA E FIXA LARGURA (IGUAL NO PC E CELULAR) */
.block-container {
    max-width: 420px;
    padding-top: 20px;
    margin: auto;
}

/* DISPLAY */
.display {
    background: #111827;
    padding: 25px;
    border-radius: 18px;
    font-size: 32px;
    text-align: right;
    margin-bottom: 15px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.5);
    min-height: 60px;
}

/* BOTÕES GRANDES */
.stButton>button {
    width: 100%;
    height: 75px;
    font-size: 22px;
    font-weight: bold;
    border-radius: 16px;
    border: none;
    transition: 0.15s;
    color: white;
}

/* NÚMEROS */
div[data-testid="column"] button {
    background: #1f2937;
}

/* HOVER */
.stButton>button:hover {
    transform: scale(1.03);
}

/* OPERADORES */
.op button {
    background: #f97316 !important;
}

/* IGUAL */
.eq button {
    background: #22c55e !important;
}

/* FUNÇÕES */
.fn button {
    background: #3b82f6 !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# ESTADO
# =========================
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "history" not in st.session_state:
    st.session_state.history = []

if "mem" not in st.session_state:
    st.session_state.mem = 0

# =========================
# SEGURANÇA
# =========================
def safe_eval(expr):
    expr = expr.replace("×", "*").replace("÷", "/")

    if not re.match(r"^[0-9+\-*/(). ]*$", expr):
        return "Erro"

    try:
        return eval(expr, {"__builtins__": None}, {})
    except:
        return "Erro"

# =========================
# DISPLAY
# =========================
st.title("Calculadora Pro")

st.markdown(f"""
<div class="display">
{st.session_state.expr if st.session_state.expr else "0"}
</div>
""", unsafe_allow_html=True)

# =========================
# FUNÇÕES AUX
# =========================
def add(v):
    st.session_state.expr += str(v)

def clear():
    st.session_state.expr = ""

def back():
    st.session_state.expr = st.session_state.expr[:-1]

# =========================
# TECLADO (GRANDE E FIXO)
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.button("C", on_click=clear)
col2.button("⌫", on_click=back)
col3.button("%", on_click=lambda: add("%"))
col4.button("÷", on_click=lambda: add("÷"))

col1, col2, col3, col4 = st.columns(4)
col1.button("7", on_click=lambda: add("7"))
col2.button("8", on_click=lambda: add("8"))
col3.button("9", on_click=lambda: add("9"))
col4.button("×", on_click=lambda: add("×"))

col1, col2, col3, col4 = st.columns(4)
col1.button("4", on_click=lambda: add("4"))
col2.button("5", on_click=lambda: add("5"))
col3.button("6", on_click=lambda: add("6"))
col4.button("-", on_click=lambda: add("-"))

col1, col2, col3, col4 = st.columns(4)
col1.button("1", on_click=lambda: add("1"))
col2.button("2", on_click=lambda: add("2"))
col3.button("3", on_click=lambda: add("3"))
col4.button("+", on_click=lambda: add("+"))

col1, col2, col3, col4 = st.columns(4)
col1.button("0", on_click=lambda: add("0"))
col2.button(".", on_click=lambda: add("."))
col3.button("M+", on_click=lambda: st.session_state.update(mem=st.session_state.mem + (safe_eval(st.session_state.expr) if st.session_state.expr else 0)))
col4.button("=", on_click=lambda: (
    st.session_state.history.append(f"{st.session_state.expr}={safe_eval(st.session_state.expr)}"),
    st.session_state.__setattr__("expr", str(safe_eval(st.session_state.expr)))
))

# =========================
# MEMÓRIA
# =========================
colA, colB = st.columns(2)

colA.button("MR", on_click=lambda: add(st.session_state.mem))
colB.button("MC", on_click=lambda: st.session_state.update(mem=0))

# =========================
# HISTÓRICO
# =========================
st.markdown("---")
st.subheader("Histórico")

if st.button("Limpar histórico"):
    st.session_state.history = []

for item in st.session_state.history[-10:]:
    st.write(item)
