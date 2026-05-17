import streamlit as st
import math
import re

st.set_page_config(
    page_title="Calculator Ultra Pro",
    layout="centered"
)

# =========================
# ESTILO PROFISSIONAL
# =========================
st.markdown("""
<style>

.stApp {
    background: radial-gradient(circle at top, #0b1020, #05060c);
    color: white;
}

/* DISPLAY */
.display {
    background: #0f172a;
    padding: 20px;
    border-radius: 16px;
    font-size: 28px;
    text-align: right;
    margin-bottom: 10px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
}

/* BOTÕES */
.stButton>button {
    width: 100%;
    height: 65px;
    border-radius: 14px;
    border: none;
    font-size: 20px;
    font-weight: bold;
    background: linear-gradient(135deg, #1e293b, #334155);
    color: white;
    transition: 0.15s ease-in-out;
}

.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(135deg, #2563eb, #7c3aed);
}

/* BOTÕES OPERADORES */
.op button {
    background: linear-gradient(135deg, #f97316, #ef4444) !important;
}

/* BOTÃO IGUAL */
.eq button {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
}

/* HISTÓRICO */
.history {
    background: #0f172a;
    padding: 12px;
    border-radius: 12px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# ESTADO
# =========================
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "mem" not in st.session_state:
    st.session_state.mem = 0

if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# FUNÇÃO SEGURA DE CÁLCULO
# =========================
def safe_eval(expression):
    expression = expression.replace("×", "*").replace("÷", "/")

    if not re.match(r"^[0-9+\-*/(). ]*$", expression):
        return "Erro"

    try:
        return eval(expression, {"__builtins__": None}, math.__dict__)
    except:
        return "Erro"

# =========================
# DISPLAY
# =========================
st.title("Calculator Ultra Pro")

st.markdown(f"""
<div class="display">
{st.session_state.expr if st.session_state.expr else "0"}
</div>
""", unsafe_allow_html=True)

# =========================
# BOTÕES
# =========================
col1, col2, col3, col4 = st.columns(4)

def add(v):
    st.session_state.expr += str(v)

def clear():
    st.session_state.expr = ""

def back():
    st.session_state.expr = st.session_state.expr[:-1]

# LINHA 1
col1.button("C", on_click=clear)
col2.button("⌫", on_click=back)
col3.button("%", on_click=lambda: add("%"))
col4.button("÷", on_click=lambda: add("÷"))

# LINHA 2
c1, c2, c3, c4 = st.columns(4)
c1.button("7", on_click=lambda: add("7"))
c2.button("8", on_click=lambda: add("8"))
c3.button("9", on_click=lambda: add("9"))
c4.button("×", on_click=lambda: add("×"))

# LINHA 3
d1, d2, d3, d4 = st.columns(4)
d1.button("4", on_click=lambda: add("4"))
d2.button("5", on_click=lambda: add("5"))
d3.button("6", on_click=lambda: add("6"))
d4.button("-", on_click=lambda: add("-"))

# LINHA 4
e1, e2, e3, e4 = st.columns(4)
e1.button("1", on_click=lambda: add("1"))
e2.button("2", on_click=lambda: add("2"))
e3.button("3", on_click=lambda: add("3"))
e4.button("+", on_click=lambda: add("+"))

# LINHA 5
f1, f2, f3, f4 = st.columns(4)
f1.button("0", on_click=lambda: add("0"))
f2.button(".", on_click=lambda: add("."))
f3.button("M+", on_click=lambda: st.session_state.update(mem=st.session_state.mem + safe_eval(st.session_state.expr) if st.session_state.expr else st.session_state.mem))
f4.button("=", on_click=lambda: (
    st.session_state.history.append(st.session_state.expr + "=" + str(safe_eval(st.session_state.expr))),
    st.session_state.__setattr__("expr", str(safe_eval(st.session_state.expr)))
))

# =========================
# MEMÓRIA
# =========================
colA, colB = st.columns(2)

if colA.button("MR"):
    st.session_state.expr += str(st.session_state.mem)

if colB.button("MC"):
    st.session_state.mem = 0

# =========================
# HISTÓRICO
# =========================
st.markdown("---")
st.subheader("Histórico")

if st.button("Limpar histórico"):
    st.session_state.history = []

st.markdown('<div class="history">', unsafe_allow_html=True)

for item in st.session_state.history[-10:]:
    st.write(item)

st.markdown('</div>', unsafe_allow_html=True)
