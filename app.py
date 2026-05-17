import streamlit as st
import math
import re

st.set_page_config(page_title="Calculadora Pro", layout="centered")

# =========================
# ESTADO
# =========================
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "history" not in st.session_state:
    st.session_state.history = []

if "mem" not in st.session_state:
    st.session_state.mem = 0

if "menu" not in st.session_state:
    st.session_state.menu = False

# =========================
# CSS FORTE (RESPONSIVO REAL)
# =========================
st.markdown("""
<style>

.stApp {
    background: #0b0f1a;
    color: white;
}

/* LARGURA FIXA (IGUAL EM QUALQUER TELA) */
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
    font-size: 30px;
    text-align: right;
    margin-bottom: 10px;
}

/* GRID REAL DE BOTÕES (NÃO STREAMLIT COLUMNS) */
.grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
}

/* BOTÕES GRANDES */
button[kind="secondary"] {
    height: 70px !important;
    font-size: 20px !important;
    border-radius: 14px !important;
    border: none !important;
}

/* CORES POR FUNÇÃO */
.num button { background: #1f2937 !important; color: white; }
.op button { background: #f97316 !important; color: white; }
.eq button { background: #22c55e !important; color: white; }
.fun button { background: #3b82f6 !important; color: white; }

/* MENU LATERAL */
.menu {
    position: fixed;
    top: 10px;
    left: 10px;
    background: #111827;
    padding: 10px;
    border-radius: 10px;
}

.menu-panel {
    background: #0f172a;
    padding: 10px;
    border-radius: 10px;
    margin-top: 10px;
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
# MENU HAMBURGUER
# =========================
colA, colB = st.columns([1, 5])

with colA:
    if st.button("☰"):
        st.session_state.menu = not st.session_state.menu

st.title("Calculadora Pro")

# MENU LATERAL
if st.session_state.menu:
    st.markdown('<div class="menu-panel">', unsafe_allow_html=True)

    if st.button("Logaritmo"):
        st.session_state.menu_mode = "log"

    if st.button("Conversor Temperatura"):
        st.session_state.menu_mode = "temp"

    if st.button("Conversor Medidas"):
        st.session_state.menu_mode = "med"

    if st.button("Memória"):
        st.session_state.menu_mode = "mem"

    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# DISPLAY
# =========================
st.markdown(f'<div class="display">{st.session_state.expr or "0"}</div>', unsafe_allow_html=True)

# =========================
# CALCULADORA (GRID FIXO REAL)
# =========================
grid = st.container()

with grid:

    cols = st.columns(4)

    cols[0].button("C", on_click=clear)
    cols[1].button("⌫", on_click=back)
    cols[2].button("%", on_click=lambda: add("%"))
    cols[3].button("÷", on_click=lambda: add("÷"))

    cols = st.columns(4)
    cols[0].button("7", on_click=lambda: add("7"))
    cols[1].button("8", on_click=lambda: add("8"))
    cols[2].button("9", on_click=lambda: add("9"))
    cols[3].button("×", on_click=lambda: add("×"))

    cols = st.columns(4)
    cols[0].button("4", on_click=lambda: add("4"))
    cols[1].button("5", on_click=lambda: add("5"))
    cols[2].button("6", on_click=lambda: add("6"))
    cols[3].button("-", on_click=lambda: add("-"))

    cols = st.columns(4)
    cols[0].button("1", on_click=lambda: add("1"))
    cols[1].button("2", on_click=lambda: add("2"))
    cols[2].button("3", on_click=lambda: add("3"))
    cols[3].button("+", on_click=lambda: add("+"))

    cols = st.columns(4)
    cols[0].button("0", on_click=lambda: add("0"))
    cols[1].button(".", on_click=lambda: add("."))

    cols[2].button("M+", on_click=lambda: st.session_state.update(mem=st.session_state.mem + (safe_eval(st.session_state.expr) if st.session_state.expr else 0)))

    cols[3].button("=", on_click=lambda: (
        st.session_state.history.append(f"{st.session_state.expr}={safe_eval(st.session_state.expr)}"),
        st.session_state.__setattr__("expr", str(safe_eval(st.session_state.expr)))
    ))

# =========================
# FUNÇÕES EXTRAS
# =========================
if hasattr(st.session_state, "menu_mode"):

    if st.session_state.menu_mode == "log":
        n = st.number_input("Log base 10", value=1.0)
        if st.button("Calcular log"):
            r = math.log10(n)
            st.session_state.history.append(f"log({n})={r}")
            st.success(r)

    if st.session_state.menu_mode == "temp":
        t = st.number_input("Temperatura", value=0.0)
        tipo = st.selectbox("Tipo", ["C→F", "F→C", "C→K"])
        if st.button("Converter"):
            if tipo == "C→F":
                r = (t*9/5)+32
            elif tipo == "F→C":
                r = (t-32)*5/9
            else:
                r = t+273.15
            st.success(r)

    if st.session_state.menu_mode == "med":
        m = st.number_input("Metros", value=1.0)
        if st.button("Converter"):
            st.success(f"{m} m = {m*100} cm")

    if st.session_state.menu_mode == "mem":
        st.write("Memória:", st.session_state.mem)
        if st.button("MC"):
            st.session_state.mem = 0
        if st.button("MR"):
            st.session_state.expr += str(st.session_state.mem)

# =========================
# HISTÓRICO
# =========================
st.markdown("---")
st.subheader("Histórico")

if st.button("Limpar histórico"):
    st.session_state.history = []

for item in st.session_state.history[-10:]:
    st.write(item)
