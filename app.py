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

if "mem" not in st.session_state:
    st.session_state.mem = 0

# =========================
# ESTILO RETRÔ PIXEL
# =========================
st.markdown("""
<style>

.stApp {
    background: #050914;
    color: #7dd3fc;
    font-family: monospace;
}

/* ASSINATURA HP */
.hp {
    font-size: 12px;
    color: #38bdf8;
    opacity: 0.8;
    margin-bottom: 5px;
}

/* TÍTULO RETRÔ */
h1 {
    color: #38bdf8;
    text-align: center;
    font-weight: 400;
    letter-spacing: 2px;
}

/* DISPLAY RETRÔ */
.display {
    background: #0b1220;
    border: 1px solid #38bdf8;
    padding: 20px;
    border-radius: 6px;
    font-size: 28px;
    text-align: right;
    margin-bottom: 10px;
    box-shadow: 0 0 10px #38bdf8;
}

/* BOTÕES PIXEL */
.stButton>button {
    background: #0b1220;
    color: #7dd3fc;
    border: 1px solid #38bdf8;
    height: 55px;
    border-radius: 4px;
    font-size: 16px;
}

.stButton>button:hover {
    background: #38bdf8;
    color: #0b1220;
}

/* HISTÓRICO */
.history {
    margin-top: 10px;
    padding: 10px;
    border: 1px dashed #38bdf8;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# ASSINATURA
# =========================
st.markdown('<div class="hp">hp // pyhetr00 system</div>', unsafe_allow_html=True)

# =========================
# TÍTULO
# =========================
st.title("calculadora barra app")

# =========================
# FUNÇÕES
# =========================
def add(x):
    st.session_state.expr = st.session_state.get("expr", "") + str(x)

def clear():
    st.session_state.expr = ""

def calc(expr):
    try:
        return eval(expr, {"__builtins__": None}, {})
    except:
        return "erro"

# init expr
if "expr" not in st.session_state:
    st.session_state.expr = ""

# =========================
# DISPLAY
# =========================
st.markdown(f"""
<div class="display">
{st.session_state.expr or "0"}
</div>
""", unsafe_allow_html=True)

# =========================
# CALCULADORA BASE
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
# FUNÇÕES RETRÔ EXTRAS
# =========================
st.markdown("---")

col1, col2, col3 = st.columns(3)

n = st.number_input("valor", value=1.0)

if col1.button("√"):
    r = math.sqrt(n)
    st.session_state.history.append(f"√{n} = {r}")
    st.session_state.expr = str(r)

if col2.button("x²"):
    r = n ** 2
    st.session_state.history.append(f"{n}² = {r}")
    st.session_state.expr = str(r)

if col3.button("log"):
    r = math.log10(n)
    st.session_state.history.append(f"log {n} = {r}")
    st.session_state.expr = str(r)

col1, col2, col3 = st.columns(3)

if col1.button("!"):
    r = math.factorial(int(n))
    st.session_state.history.append(f"{n}! = {r}")
    st.session_state.expr = str(r)

if col2.button("%"):
    r = n / 100
    st.session_state.history.append(f"{n}% = {r}")
    st.session_state.expr = str(r)

if col3.button("³√"):
    r = n ** (1/3)
    st.session_state.history.append(f"³√{n} = {r}")
    st.session_state.expr = str(r)

# =========================
# HISTÓRICO
# =========================
st.markdown("---")
st.subheader("history log")

if st.button("clear history"):
    st.session_state.history = []

st.markdown('<div class="history">', unsafe_allow_html=True)

for h in st.session_state.history[-10:]:
    st.write(h)

st.markdown("</div>", unsafe_allow_html=True)
