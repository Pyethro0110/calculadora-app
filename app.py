import streamlit as st
import math
import re

st.set_page_config(page_title="Calc Mobile", layout="centered")

# =========================
# STATE
# =========================
if "page" not in st.session_state:
    st.session_state.page = "calc"

if "expr" not in st.session_state:
    st.session_state.expr = ""

if "history" not in st.session_state:
    st.session_state.history = []

if "menu" not in st.session_state:
    st.session_state.menu = False

# =========================
# MOBILE-FIRST CSS
# =========================
st.markdown("""
<style>

.stApp {
    background: #0a0c10;
    color: white;
}

/* FORÇA MOBILE FIRST */
.block-container {
    max-width: 100vw;
    padding: 10px;
}

/* APP BAR */
.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
}

/* DISPLAY GRANDE */
.display {
    background: #121826;
    padding: 25px;
    font-size: 34px;
    border-radius: 20px;
    text-align: right;
    margin-bottom: 12px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.4);
}

/* BOTÕES GRANDES MOBILE */
button {
    height: 78px !important;
    font-size: 24px !important;
    border-radius: 18px !important;
    font-weight: 600 !important;
}

/* NÚMEROS */
div[data-testid="stButton"] button {
    background: #1f2937;
    color: white;
}

/* OPERADORES */
.op button {
    background: #ff6b00 !important;
}

/* IGUAL */
.eq button {
    background: #00c853 !important;
}

/* MENU LATERAL (DRAWER SIMULADO) */
.drawer {
    position: fixed;
    top: 0;
    left: 0;
    width: 75%;
    height: 100%;
    background: #0f172a;
    padding: 20px;
    transform: translateX(-100%);
    transition: 0.3s ease-in-out;
    z-index: 999;
}

.drawer.open {
    transform: translateX(0);
}

/* FUNDO ESCURO QUANDO MENU ABRE */
.overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.6);
}

/* HISTÓRICO LATERAL */
.history {
    background: #111827;
    padding: 10px;
    border-radius: 12px;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# FUNCTIONS
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
# HEADER (APP STYLE)
# =========================
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("≡"):
        st.session_state.menu = not st.session_state.menu

with col3:
    if st.button("⌫"):
        back()

# =========================
# DRAWER MENU
# =========================
if st.session_state.menu:
    st.markdown('<div class="overlay"></div>', unsafe_allow_html=True)

    st.markdown('<div class="drawer open">', unsafe_allow_html=True)

    st.subheader("Menu")

    if st.button("Logaritmo"):
        st.session_state.page = "log"
        st.session_state.menu = False

    if st.button("Temperatura"):
        st.session_state.page = "temp"
        st.session_state.menu = False

    if st.button("Conversor"):
        st.session_state.page = "conv"
        st.session_state.menu = False

    if st.button("Memória"):
        st.session_state.page = "mem"
        st.session_state.menu = False

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# CALCULADORA PRINCIPAL
# =========================
if st.session_state.page == "calc":

    st.title("Calculator")

    st.markdown(f"""
    <div class="display">
    {st.session_state.expr or "0"}
    </div>
    """, unsafe_allow_html=True)

    # GRID MOBILE
    col = st.columns(4)

    col[0].button("C", on_click=clear)
    col[1].button("%", on_click=lambda: add("%"))
    col[2].button("÷", on_click=lambda: add("÷"))
    col[3].button("×", on_click=lambda: add("×"))

    col = st.columns(4)
    col[0].button("7", on_click=lambda: add("7"))
    col[1].button("8", on_click=lambda: add("8"))
    col[2].button("9", on_click=lambda: add("9"))
    col[3].button("-", on_click=lambda: add("-"))

    col = st.columns(4)
    col[0].button("4", on_click=lambda: add("4"))
    col[1].button("5", on_click=lambda: add("5"))
    col[2].button("6", on_click=lambda: add("6"))
    col[3].button("+", on_click=lambda: add("+"))

    col = st.columns(4)
    col[0].button("1", on_click=lambda: add("1"))
    col[1].button("2", on_click=lambda: add("2"))
    col[2].button("3", on_click=lambda: add("3"))

    if col[3].button("="):
        result = safe_eval(st.session_state.expr)
        st.session_state.history.append(f"{st.session_state.expr}={result}")
        st.session_state.expr = str(result)

    col = st.columns(4)
    col[0].button("0", on_click=lambda: add("0"))
    col[1].button(".", on_click=lambda: add("."))

# =========================
# LOG
# =========================
elif st.session_state.page == "log":
    n = st.number_input("Log base 10", value=1.0)

    if st.button("Calcular"):
        r = math.log10(n)
        st.session_state.history.append(f"log({n})={r}")
        st.session_state.page = "calc"
        st.success(r)

# =========================
# TEMPERATURA
# =========================
elif st.session_state.page == "temp":
    t = st.number_input("Temperatura", value=0.0)
    tipo = st.selectbox("Tipo", ["C→F", "F→C", "C→K"])

    if st.button("Converter"):
        if tipo == "C→F":
            r = (t*9/5)+32
        elif tipo == "F→C":
            r = (t-32)*5/9
        else:
            r = t+273.15

        st.session_state.history.append(f"Temp={r}")
        st.session_state.page = "calc"
        st.success(r)

# =========================
# CONVERSOR
# =========================
elif st.session_state.page == "conv":
    m = st.number_input("Metros", value=1.0)

    if st.button("Converter"):
        st.success(f"{m} m = {m*100} cm")
        st.session_state.page = "calc"

# =========================
# MEMÓRIA
# =========================
elif st.session_state.page == "mem":
    st.write("Memória:", st.session_state.mem)

    if st.button("MC"):
        st.session_state.mem = 0

    if st.button("MR"):
        st.session_state.expr += str(st.session_state.mem)

    if st.button("Voltar"):
        st.session_state.page = "calc"

# =========================
# HISTÓRICO (FIXO MOBILE)
# =========================
st.markdown("---")
st.subheader("Histórico")

if st.button("Limpar histórico"):
    st.session_state.history = []

for item in st.session_state.history[-10:]:
    st.write(item)
