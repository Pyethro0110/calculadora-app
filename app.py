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

if "expr" not in st.session_state:
    st.session_state.expr = ""

# =========================
# ESTILO RETRÔ MODERNO
# =========================
st.markdown("""
<style>

.stApp {
    background: #050914;
    color: #7dd3fc;
    font-family: monospace;
}

/* ASSINATURA */
.hp {
    font-size: 12px;
    color: #38bdf8;
    opacity: 0.8;
}

/* TÍTULO */
h1 {
    text-align: center;
    color: #38bdf8;
    font-weight: 400;
    letter-spacing: 2px;
}

/* DISPLAY */
.display {
    background: #0b1220;
    border: 1px solid #38bdf8;
    padding: 18px;
    border-radius: 6px;
    font-size: 30px;
    text-align: right;
    margin-bottom: 10px;
}

/* BOTÕES */
.stButton>button {
    background: #0b1220;
    color: #7dd3fc;
    border: 1px solid #38bdf8;
    height: 55px;
    font-size: 16px;
    border-radius: 5px;
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
st.markdown('<div class="hp">hp // system core</div>', unsafe_allow_html=True)

# =========================
# TÍTULO
# =========================
st.title("calculadora-app")

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
# TECLADO BÁSICO
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
# FUNÇÕES EXTRAS
# =========================
st.markdown("---")

n = st.number_input("valor", value=1.0)

c1, c2, c3 = st.columns(3)

if c1.button("√"):
    r = math.sqrt(n)
    st.session_state.expr = str(r)
    st.session_state.history.append(f"√{n} = {r}")

if c2.button("x²"):
    r = n ** 2
    st.session_state.expr = str(r)
    st.session_state.history.append(f"{n}² = {r}")

if c3.button("log"):
    r = math.log10(n)
    st.session_state.expr = str(r)
    st.session_state.history.append(f"log({n}) = {r}")

c1, c2, c3 = st.columns(3)

if c1.button("!"):
    r = math.factorial(int(n))
    st.session_state.expr = str(r)
    st.session_state.history.append(f"{n}! = {r}")

if c2.button("%"):
    r = n / 100
    st.session_state.expr = str(r)
    st.session_state.history.append(f"{n}% = {r}")

if c3.button("³√"):
    r = n ** (1/3)
    st.session_state.expr = str(r)
    st.session_state.history.append(f"³√{n} = {r}")

# =========================
# HISTÓRICO
# =========================
st.markdown("---")
st.subheader("history")

if st.button("clear history"):
    st.session_state.history = []

for item in st.session_state.history[-10:]:
    st.write(item)
