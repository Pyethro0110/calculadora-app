import streamlit as st
import math
import re

st.set_page_config(page_title="Calc Mobile Fix", layout="centered")

# =========================
# STATE
# =========================
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "history" not in st.session_state:
    st.session_state.history = []

if "mem" not in st.session_state:
    st.session_state.mem = 0


# =========================
# CSS REAL (CORRIGE MOBILE)
# =========================
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background: #0a0c10;
    color: white;
}

/* CENTRALIZA E EVITA QUEBRA NO CELULAR */
.block-container {
    max-width: 420px;
    margin: auto;
    padding-top: 10px;
}

/* DISPLAY */
.display {
    background: #111827;
    padding: 22px;
    border-radius: 16px;
    font-size: 32px;
    text-align: right;
    margin-bottom: 12px;
    word-break: break-all;
}

/* GRID REAL (EVITA LINHA ÚNICA BUGADA) */
.calc-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
}

/* BOTÕES GIGANTES */
button {
    height: 72px !important;
    font-size: 22px !important;
    border-radius: 14px !important;
    font-weight: bold !important;
}

/* NÚMEROS (PRETO/CINZA ESCURO) */
div[data-testid="stButton"] button {
    background: #111111 !important;
    color: white !important;
}

/* OPERAÇÕES (VERMELHO) */
.op button {
    background: #ef4444 !important;
    color: white !important;
}

/* IGUAL (VERDE) */
.eq button {
    background: #22c55e !important;
}

/* FUNÇÕES (AZUL) */
.fn button {
    background: #3b82f6 !important;
}

/* HISTÓRICO LIMPO */
.history {
    background: #0f172a;
    padding: 12px;
    border-radius: 12px;
    margin-top: 10px;
    word-break: break-word;
}

</style>
""", unsafe_allow_html=True)


# =========================
# FUNÇÕES
# =========================
def add(v):
    st.session_state.expr += str(v)

def clear():
    st.session_state.expr = ""

def back():
    st.session_state.expr = st.session_state.expr[:-1]

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
st.title("Calculadora Mobile Fix")

st.markdown(f"""
<div class="display">
{st.session_state.expr if st.session_state.expr else "0"}
</div>
""", unsafe_allow_html=True)


# =========================
# TECLADO (GRID REAL — SEM BUG MOBILE)
# =========================
st.markdown('<div class="calc-grid">', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button("C", on_click=clear)

with c2:
    st.button("⌫", on_click=back)

with c3:
    st.button("÷", on_click=lambda: add("÷"))

with c4:
    st.button("×", on_click=lambda: add("×"))

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button("7", on_click=lambda: add("7"))

with c2:
    st.button("8", on_click=lambda: add("8"))

with c3:
    st.button("9", on_click=lambda: add("9"))

with c4:
    st.button("-", on_click=lambda: add("-"))

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button("4", on_click=lambda: add("4"))

with c2:
    st.button("5", on_click=lambda: add("5"))

with c3:
    st.button("6", on_click=lambda: add("6"))

with c4:
    st.button("+", on_click=lambda: add("+"))

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button("1", on_click=lambda: add("1"))

with c2:
    st.button("2", on_click=lambda: add("2"))

with c3:
    st.button("3", on_click=lambda: add("3"))

with c4:
    if st.button("="):
        result = safe_eval(st.session_state.expr)
        st.session_state.history.append(f"{st.session_state.expr} = {result}")
        st.session_state.expr = str(result)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.button("0", on_click=lambda: add("0"))

with c2:
    st.button(".", on_click=lambda: add("."))

with c3:
    st.button("M+", on_click=lambda: st.session_state.update(mem=st.session_state.mem + (safe_eval(st.session_state.expr) if st.session_state.expr else 0)))

with c4:
    st.button("%", on_click=lambda: add("%"))


st.markdown('</div>', unsafe_allow_html=True)


# =========================
# HISTÓRICO (CORRIGIDO)
# =========================
st.markdown("---")
st.subheader("Histórico")

if st.button("Limpar histórico"):
    st.session_state.history = []

st.markdown('<div class="history">', unsafe_allow_html=True)

for item in st.session_state.history[-10:]:
    st.write(item)

st.markdown('</div>', unsafe_allow_html=True)
